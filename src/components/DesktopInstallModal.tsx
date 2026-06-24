import { Download, MoreVertical, X } from "lucide-react";
import { motion } from "motion/react";

type DesktopInstallModalProps = {
  isOpen: boolean;
  onClose: () => void;
};

export function DesktopInstallModal({ isOpen, onClose }: DesktopInstallModalProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
        className="absolute inset-0 bg-[#3f342d]/40 backdrop-blur-md"
      />

      <motion.div
        initial={{ opacity: 0, scale: 0.96, y: 18 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.96, y: 18 }}
        transition={{ type: "spring", duration: 0.35 }}
        className="font-hand relative z-10 w-full max-w-md overflow-hidden rounded-[2rem] border border-[#efd9d0] bg-[#fff8f4] p-6 shadow-[0_24px_70px_rgba(118,91,78,0.28)]"
      >
        <div className="pointer-events-none absolute inset-0 z-0 journal-paper opacity-50" />

        <div className="relative z-10">
          <button
            type="button"
            onClick={onClose}
            className="absolute -right-1 -top-1 flex h-9 w-9 items-center justify-center rounded-full border border-[#efd9d0] bg-white/80 text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
            aria-label="關閉"
          >
            <X size={18} />
          </button>

          <div className="mb-5 text-center">
            <h3 className="text-xl font-bold text-[#3f342d]">加入桌面</h3>
            <p className="mt-1.5 text-sm leading-6 text-[#8b7666]">
              Chrome 有時會把安裝入口放在網址列或右上角選單裡。
            </p>
          </div>

          <div className="space-y-4">
            <div className="flex gap-4 rounded-[1.2rem] border border-white/60 bg-white/45 p-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#e8f4ee] text-[#355249]">
                <Download size={18} />
              </div>
              <div className="flex-1 text-sm leading-7 text-[#52433d]">
                先看網址列右側有沒有「安裝」圖示，點它就可以把 Ariel's Med 加到桌面。
              </div>
            </div>

            <div className="flex gap-4 rounded-[1.2rem] border border-white/60 bg-white/45 p-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#fff0f6] text-[#9a496b]">
                <MoreVertical size={18} />
              </div>
              <div className="flex-1 text-sm leading-7 text-[#52433d]">
                如果沒看到圖示，請點 Chrome 右上角三個點，找「投放、儲存及分享」或「安裝頁面」。
              </div>
            </div>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="mt-6 flex h-11 w-full items-center justify-center rounded-xl bg-[#b8e2d4] font-bold text-[#355249] transition hover:bg-[#a5d9c7] active:scale-[0.98]"
          >
            我知道了
          </button>
        </div>
      </motion.div>
    </div>
  );
}
