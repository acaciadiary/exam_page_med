import { useMemo } from "react";

type PerformanceStat = {
  label: string;
  answered: number;
  correct: number;
  accuracy: number;
};

type RadarChartProps = {
  stats: PerformanceStat[];
  activeStage: "stage-1" | "stage-2";
  theme: "light" | "dark" | "clinical";
};

export function RadarChart({ stats, activeStage, theme }: RadarChartProps) {
  // Define axes based on stage
  const axes = useMemo(() => {
    if (activeStage === "stage-1") {
      return ["醫學一", "醫學二", "總平均"];
    } else {
      return ["醫學三", "醫學四", "醫學五", "醫學六"];
    }
  }, [activeStage]);

  // Calculate values for each axis
  const chartData = useMemo(() => {
    return axes.map((axisName) => {
      if (axisName === "總平均") {
        // Calculate average accuracy of stage-1 subjects
        const stage1Stats = stats.filter(
          (s) => s.label === "醫學一" || s.label === "醫學二"
        );
        const totalAnswered = stage1Stats.reduce((sum, s) => sum + s.answered, 0);
        const totalCorrect = stage1Stats.reduce((sum, s) => sum + s.correct, 0);
        const accuracy =
          totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;

        return {
          name: axisName,
          value: accuracy,
          answered: totalAnswered,
        };
      }

      const stat = stats.find((s) => s.label === axisName);
      return {
        name: axisName,
        value: stat ? stat.accuracy : 0,
        answered: stat ? stat.answered : 0,
      };
    });
  }, [axes, stats]);

  // SVG Geometry parameters
  const size = 230;
  const center = size / 2;
  const radius = 70; // Max radius for 100% value
  const numAxes = axes.length;

  // Compute coordinates for a value at a specific axis index
  const getCoordinates = (index: number, val: number) => {
    const angle = (index * 2 * Math.PI) / numAxes - Math.PI / 2;
    const distance = (val / 100) * radius;
    const x = center + distance * Math.cos(angle);
    const y = center + distance * Math.sin(angle);
    return { x, y, angle };
  };

  // Grid lines levels: 25%, 50%, 75%, 100%
  const gridLevels = [25, 50, 75, 100];

  // Colors based on theme
  const colors = useMemo(() => {
    switch (theme) {
      case "dark":
        return {
          grid: "rgba(255, 255, 255, 0.08)",
          gridText: "#a2949e",
          axis: "rgba(255, 255, 255, 0.08)",
          polygonFill: "rgba(243, 166, 196, 0.18)",
          polygonStroke: "#f3a6c4",
          label: "#dccbd3",
          centerDot: "#f3a6c4",
        };
      case "clinical":
        return {
          grid: "rgba(39, 86, 125, 0.09)",
          gridText: "#5b6f82",
          axis: "rgba(39, 86, 125, 0.09)",
          polygonFill: "rgba(30, 144, 255, 0.12)",
          polygonStroke: "#1f4e79",
          label: "#26384a",
          centerDot: "#1f4e79",
        };
      case "light":
      default:
        return {
          grid: "rgba(180, 137, 118, 0.14)",
          gridText: "#a68e98",
          axis: "rgba(180, 137, 118, 0.14)",
          polygonFill: "rgba(246, 169, 198, 0.26)",
          polygonStroke: "#b36a84",
          label: "#5c4940",
          centerDot: "#b36a84",
        };
    }
  }, [theme]);

  // Render path for the data polygon
  const dataPoints = chartData.map((d, i) => getCoordinates(i, d.value));
  const dataPolygonPoints = dataPoints.map((p) => `${p.x},${p.y}`).join(" ");

  return (
    <div className="flex justify-center items-center">
      <svg
        width={size}
        height={size}
        viewBox={`0 0 ${size} ${size}`}
        className="overflow-visible select-none"
      >
        {/* Render Grid Polygons */}
        {gridLevels.map((level) => {
          const points = Array.from({ length: numAxes }, (_, i) => {
            const p = getCoordinates(i, level);
            return `${p.x},${p.y}`;
          }).join(" ");

          return (
            <polygon
              key={level}
              points={points}
              fill="none"
              stroke={colors.grid}
              strokeWidth={1}
            />
          );
        })}

        {/* Render Level text tags (e.g. 50%, 100% on the vertical top axis) */}
        {gridLevels.map((level) => {
          const p = getCoordinates(0, level); // Align along axis 0 (top vertical)
          return (
            <text
              key={`level-txt-${level}`}
              x={p.x + 4}
              y={p.y + 3}
              fontSize={8}
              fontWeight="bold"
              fill={colors.gridText}
              className="opacity-70"
            >
              {level}%
            </text>
          );
        })}

        {/* Render Axis lines */}
        {Array.from({ length: numAxes }).map((_, i) => {
          const outerPoint = getCoordinates(i, 100);
          return (
            <line
              key={`axis-line-${i}`}
              x1={center}
              y1={center}
              x2={outerPoint.x}
              y2={outerPoint.y}
              stroke={colors.axis}
              strokeWidth={1.2}
            />
          );
        })}

        {/* Render Data Polygon */}
        {dataPoints.length > 0 && (
          <polygon
            points={dataPolygonPoints}
            fill={colors.polygonFill}
            stroke={colors.polygonStroke}
            strokeWidth={2}
            strokeLinejoin="round"
          />
        )}

        {/* Render Data Points (dots on vertices) */}
        {dataPoints.map((p, i) => (
          <circle
            key={`data-dot-${i}`}
            cx={p.x}
            cy={p.y}
            r={3.5}
            fill={colors.polygonStroke}
          />
        ))}

        {/* Center dot */}
        <circle cx={center} cy={center} r={2} fill={colors.centerDot} />

        {/* Render Labels */}
        {chartData.map((d, i) => {
          const p = getCoordinates(i, 100);
          const cos = Math.cos(p.angle);
          const sin = Math.sin(p.angle);

          // Calculate label distance (padded outside outer grid)
          const padDist = 16;
          const lx = center + (radius + padDist) * Math.cos(p.angle);
          const ly = center + (radius + padDist) * Math.sin(p.angle);

          // Precise alignment anchor
          const textAnchor = Math.abs(cos) < 0.1 ? "middle" : cos > 0 ? "start" : "end";
          let dy = "0.36em";
          if (sin < -0.9) dy = "-0.5em";
          else if (sin > 0.9) dy = "1.25em";

          // Format value string
          const valDisplay = d.answered > 0 ? `${d.value}%` : "-%";

          return (
            <g key={`axis-lbl-${i}`} className="font-hand">
              <text
                x={lx}
                y={ly}
                textAnchor={textAnchor}
                dy={dy}
                fontSize={11}
                fontWeight="bold"
                fill={colors.label}
              >
                {d.name}
                <tspan
                  fill={d.answered > 0 ? colors.polygonStroke : colors.gridText}
                  fontWeight="extrabold"
                  fontSize={10}
                  dx="2"
                >
                  {valDisplay}
                </tspan>
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
}
