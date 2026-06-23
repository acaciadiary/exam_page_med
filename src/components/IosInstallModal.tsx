import React from "react";
import { Share, Plus, X } from "lucide-react";
import { motion } from "motion/react";

type IosInstallModalProps = {
  isOpen: boolean;
  onClose: () => void;
};

export function IosInstallModal({ isOpen, onClose }: IosInstallModalProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
        className="absolute inset-0 bg-[#3f342d]/40 backdrop-blur-md"
      />

      {/* Modal Box */}
      <motion.div
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        transition={{ type: "spring", duration: 0.35 }}
        className="font-hand relative z-10 w-full max-w-md overflow-hidden rounded-[2rem] border border-[#efd9d0] bg-[#fff8f4] p-6 shadow-[0_24px_70px_rgba(118,91,78,0.28)]"
      >
        {/* Paper Texture Overlay */}
        <div className="pointer-events-none absolute inset-0 z-0 journal-paper opacity-50" />

        <div className="relative z-10">
          {/* Close Button */}
          <button
            type="button"
            onClick={onClose}
            className="absolute -right-1 -top-1 flex h-9 w-9 items-center justify-center rounded-full border border-[#efd9d0] bg-white/80 text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
            aria-label="關閉"
          >
            <X size={18} />
          </button>

          {/* Header */}
          <div className="mb-5 text-center">
            <h3 className="text-xl font-bold text-[#3f342d]">安裝到手機桌面</h3>
            <p className="mt-1.5 text-xs font-medium text-[#8b7666]">
              將 Ariel's Med 新增至主畫面，即可像 App 一樣全螢幕使用！
            </p>
          </div>

          {/* Steps */}
          <div className="space-y-4">
            <div className="flex gap-4 rounded-[1.2rem] border border-white/60 bg-white/40 p-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#fce8e6] text-[#c95f55] font-bold text-sm">
                1
              </div>
              <div className="flex-1 text-sm text-[#52433D] leading-relaxed">
                點擊 Safari 瀏覽器下方的
                <span className="mx-1.5 inline-flex items-center justify-center rounded-lg border border-[#efd9d0] bg-white p-1.5 text-[#9a496b] align-middle shadow-[0_2px_6px_rgba(0,0,0,0.04)]">
                  <Share size={15} />
                </span>
                <strong>「分享」</strong>按鈕。
              </div>
            </div>

            <div className="flex gap-4 rounded-[1.2rem] border border-white/60 bg-white/40 p-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#e2f1e6] text-[#428a55] font-bold text-sm">
                2
              </div>
              <div className="flex-1 text-sm text-[#52433D] leading-relaxed">
                在分享選單中向下捲動，點擊
                <span className="mx-1.5 inline-flex items-center justify-center rounded-lg border border-[#efd9d0] bg-white p-1.5 text-[#9a496b] align-middle shadow-[0_2px_6px_rgba(0,0,0,0.04)]">
                  <Plus size={15} />
                </span>
                <strong>「加入主畫面」</strong>。
              </div>
            </div>

            <div className="flex gap-4 rounded-[1.2rem] border border-white/60 bg-white/40 p-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#e6ebf5] text-[#4f6ea6] font-bold text-sm">
                3
              </div>
              <div className="flex-1 text-sm text-[#52433D] leading-relaxed">
                確認名稱為「Ariel's Med」後，點擊右上角的<strong>「新增」</strong>，即可完成安裝！
              </div>
            </div>
          </div>

          {/* Footer button */}
          <div className="mt-6">
            <button
              type="button"
              onClick={onClose}
              className="flex w-full h-11 items-center justify-center rounded-xl bg-[#b8e2d4] text-[#355249] font-bold transition hover:bg-[#a5d9c7] active:scale-[0.98] cursor-pointer"
            >
              我知道了
            </button>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
