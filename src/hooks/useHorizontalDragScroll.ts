import { useRef } from "react";

type DragState = {
  isDragging: boolean;
  pointerId: number | null;
  startX: number;
  startScrollLeft: number;
};

const DRAG_THRESHOLD = 6;

export function useHorizontalDragScroll() {
  const dragStateRef = useRef<DragState>({
    isDragging: false,
    pointerId: null,
    startX: 0,
    startScrollLeft: 0,
  });

  const onPointerDown = (event: React.PointerEvent<HTMLDivElement>) => {
    if (event.button !== 0) return;

    const container = event.currentTarget;
    dragStateRef.current = {
      isDragging: false,
      pointerId: event.pointerId,
      startX: event.clientX,
      startScrollLeft: container.scrollLeft,
    };
  };

  const onPointerMove = (event: React.PointerEvent<HTMLDivElement>) => {
    const container = event.currentTarget;
    const dragState = dragStateRef.current;
    if (dragState.pointerId !== event.pointerId) return;

    const deltaX = event.clientX - dragState.startX;
    if (!dragState.isDragging) {
      if (Math.abs(deltaX) < DRAG_THRESHOLD) return;

      dragStateRef.current.isDragging = true;
      container.dataset.dragging = "true";
      container.setPointerCapture(event.pointerId);
    }

    event.preventDefault();
    container.scrollLeft = dragState.startScrollLeft - deltaX;
  };

  const stopDragging = (container: HTMLDivElement, pointerId: number) => {
    const dragState = dragStateRef.current;
    if (dragState.pointerId !== pointerId) return;

    dragStateRef.current = {
      isDragging: false,
      pointerId: null,
      startX: 0,
      startScrollLeft: 0,
    };
    delete container.dataset.dragging;

    if (container.hasPointerCapture(pointerId)) {
      container.releasePointerCapture(pointerId);
    }
  };

  const onPointerUp = (event: React.PointerEvent<HTMLDivElement>) => {
    stopDragging(event.currentTarget, event.pointerId);
  };

  const onPointerCancel = (event: React.PointerEvent<HTMLDivElement>) => {
    stopDragging(event.currentTarget, event.pointerId);
  };

  return {
    onPointerDown,
    onPointerMove,
    onPointerUp,
    onPointerCancel,
  };
}
