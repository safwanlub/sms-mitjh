import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

type Props = {
  data: {
    bulan: string;
    total: number;
  }[];
};

export default function PelanggaranChart({ data }: Props) {
  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="bulan" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Bar dataKey="total" fill="#dc2626" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
