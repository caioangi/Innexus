import AnimationWrapper from "@/components/AnimationWrapper"

const cards = [
  {
    title: "Soluções sob medida, sempre",
    description: "Nada é genérico ou engessado. Cada projeto nasce de um diagnóstico real e entrega exatamente o que o cliente precisa."
  },
  {
    title: "Engenharia + Design + Automação",
    description: "Integramos tecnologia, UX e orquestração de processos em soluções completas, inteligentes e eficientes."
  },
  {
    title: "Operação digital contínua",
    description: "Acompanhamos, ajustamos e evoluímos tudo o que criamos. Sua operação digital nunca para de melhorar."
  }
]

export default function Diferenciais() {
  return (
    <section className="py-32 bg-[#0b0b0b]">
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
<AnimationWrapper className="text-center mb-16">
  <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] mb-4">
    Por que escolher a INNEXUS.
  </h2>
  <p className="text-lg md:text-xl text-[#a6a6a6] max-w-3xl mx-auto">
    Tecnologia de alto nível, criada sob medida para o seu negócio.
  </p>
</AnimationWrapper>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {cards.map((card, index) => (
            <AnimationWrapper key={card.title} delay={index * 120}>
              <div className="relative bg-transparent border border-[#1a1a1a] rounded-xl p-8 transition-all duration-300 group">
                <h3 className="text-2xl font-semibold text-[#f2f2f2] mb-3">{card.title}</h3>
                <p className="text-[#a6a6a6] leading-relaxed">{card.description}</p>
                <div className="absolute inset-0 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none" style={{background: "linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0) 100%)"}}></div>
              </div>
            </AnimationWrapper>
          ))}
        </div>
      </div>
    </section>
  )
}
