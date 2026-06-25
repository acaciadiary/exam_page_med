import os
import sys
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        print("Please set it in PowerShell using: $env:GEMINI_API_KEY=\"your_key_here\"")
        sys.exit(1)

    manifest_path = Path("reports/gemini_prompts/manifest.json")
    if not manifest_path.exists():
        print(f"Error: Manifest file not found at {manifest_path}.")
        print("Please generate prompts first using: python scripts/exams/export_gemini_prompts.py ...")
        sys.exit(1)

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading manifest: {e}")
        sys.exit(1)

    batches = manifest.get("batches", [])
    if not batches:
        print("No batches found in manifest.json.")
        return

    print(f"Found {len(batches)} batches in manifest.")
    print("Starting Gemini API generation...")

    # We will query gemini-1.5-flash by default
    model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

    for i, batch in enumerate(batches, start=1):
        batch_id = batch.get("batch_id")
        prompt_path = Path(batch.get("prompt_path"))
        output_path = Path(batch.get("suggested_output_path"))

        if output_path.exists():
            print(f"[{i}/{len(batches)}] Skipping {batch_id} (Output already exists at {output_path})")
            continue

        if not prompt_path.exists():
            print(f"[{i}/{len(batches)}] Error: Prompt file {prompt_path} does not exist. Skipping.")
            continue

        print(f"[{i}/{len(batches)}] Generating explanations for {batch_id}...")
        prompt_content = prompt_path.read_text(encoding="utf-8")

        # Prepare request payload
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt_content
                }]
            }],
            "generationConfig": {
                "responseMimeType": "application/json"
            }
        }

        req_data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=req_data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        success = False
        retries = 3
        backoff = 5

        while not success and retries > 0:
            try:
                with urllib.request.urlopen(req) as response:
                    res_data = response.read().decode("utf-8")
                    res_json = json.loads(res_data)
                    
                    # Extract generated text
                    candidates = res_json.get("candidates", [])
                    if not candidates:
                        raise ValueError("No candidates returned from Gemini API.")
                    
                    text_content = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    if not text_content:
                        raise ValueError("Empty text content in candidate response.")

                    # Save text_content (which should be pure JSON) to output_path
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    # Verify if it's valid JSON
                    parsed_response = json.loads(text_content)
                    output_path.write_text(json.dumps(parsed_response, ensure_ascii=False, indent=2), encoding="utf-8")
                    
                    print(f"      Success! Saved to {output_path}")
                    success = True
            except urllib.error.HTTPError as e:
                # Handle rate limiting (429) or other errors
                print(f"      HTTP Error {e.code}: {e.reason}")
                try:
                    body = e.read().decode("utf-8")
                    print(f"      Response body: {body[:300]}")
                except Exception:
                    pass
                retries -= 1
                if retries > 0:
                    print(f"      Retrying in {backoff} seconds...")
                    time.sleep(backoff)
                    backoff *= 2
            except Exception as e:
                print(f"      Error: {e}")
                retries -= 1
                if retries > 0:
                    print(f"      Retrying in {backoff} seconds...")
                    time.sleep(backoff)
                    backoff *= 2

        if not success:
            print(f"Failed to generate for {batch_id} after retries.")
            sys.exit(1)

        # Sleep to comply with RPM limits (15 RPM -> max 1 request every 4 seconds)
        if i < len(batches):
            print("      Sleeping 5 seconds to satisfy rate limits...")
            time.sleep(5)

    print("Generation complete!")

if __name__ == "__main__":
    main()
