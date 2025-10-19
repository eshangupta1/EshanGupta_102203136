/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: { extend: {
    colors: { brand: { 500: "#7c4dff", 600: "#6c3dff" } },
    boxShadow: { glow: "0 0 40px rgba(124,77,255,.25)" }
  }},
  plugins: []
}
