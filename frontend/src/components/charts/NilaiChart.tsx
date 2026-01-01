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
    kelas__nama: string;
    rata_rata: number;
  }[];
};

export default function NilaiChart({ data }: Props) {
  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="kelas__nama" />
          <YAxis domain={[0, 100]} />
          <Tooltip />
          <Bar dataKey="rata_rata" fill="#16a34a" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
