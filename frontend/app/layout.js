import "./globals.css";

export const metadata = {
  title: "Next Starter",
  description: "Minimal Next.js starter"
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
