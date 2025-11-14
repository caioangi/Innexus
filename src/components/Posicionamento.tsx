import { useScrollAnimation } from "@/hooks/useScrollAnimation"

export default function Posicionamento() {
  const isVisible = useScrollAnimation()

  return (
    <section className="py-32 bg-[#0b0b0b]" data-animate>
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
        <div className={`grid grid-cols-1 lg:grid-cols-12 gap-12 items-center transition-all duration-1000 ${isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-8"}`}>
          <div className="lg:col-span-5">
            <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] leading-tight">Tecnologia feita sob medida.</h2>
          </div>
          <div className="lg:col-span-7">
            <div className="relative pl-8 lg:pl-12">
              <div className="absolute left-0 top-0 bottom-0 w-px bg-[#1a1a1a]" />
              <p className="text-lg md:text-xl text-[#bdbdbd] leading-relaxed">Nossa missão é simples: resolver problemas reais através de soluções digitais sob medida. Nada genérico, nada engessado — apenas excelência, precisão e entrega real. </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
