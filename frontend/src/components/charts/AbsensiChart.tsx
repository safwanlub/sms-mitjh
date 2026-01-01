import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

type Props = {
  data: {
    tanggal: string;
    total: number;
  }[];
};

export default function AbsensiChart({ data }: Props) {
  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="tanggal" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="total"
            stroke="#2563eb"
            strokeWidth={3}
            dot={{ r: 4 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
