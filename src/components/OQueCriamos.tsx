import AnimationWrapper from "@/components/AnimationWrapper"

const itens = [
  "Landing pages premium",
  "Sites institucionais completos",
  "Web apps e aplicativos internos",
  "Sistemas sob medida",
  "Ferramentas personalizadas",
  "Automação via N8N",
  "Integrações com CRM / WhatsApp / APIs",
  "Dashboards e painéis gerenciais",
  "Funis digitais e fluxos de vendas",
  "Consultoria tech",
  "Otimização de processos",
  "Soluções digitais sob demanda"
]

export default function OQueCriamos() {
  return (
    <section className="py-24 bg-[#0b0b0b]">
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
        <AnimationWrapper className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] mb-4">O que criamos.</h2>
          <p className="text-lg md:text-xl text-[#bdbdbd] max-w-3xl mx-auto">Da landing ao sistema. Do fluxo simples à plataforma completa.</p>
        </AnimationWrapper>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {itens.map((titulo, index) => (
            <AnimationWrapper key={titulo} delay={index * 80}>
              <div className="relative border border-[#1a1a1a] bg-transparent p-6 md:p-7 transition-all duration-300 group">
                <h3 className="text-base md:text-lg font-semibold text-[#f2f2f2]">{titulo}</h3>
                <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none" style={{background: "linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0) 100%)"}}></div>
              </div>
            </AnimationWrapper>
          ))}
        </div>
      </div>
    </section>
  )
}
