const planos = [
  {
    nome: "START",
    preco: "R$ 179/mês",
    popular: false,
    recursos: [
      "Presença digital básica",
      "1 solução por mês",
      "1 automação simples", 
      "Suporte técnico",
      "Entrega inicial 48h"
    ]
  },
  {
    nome: "GROW",
    preco: "R$ 579/mês",
    popular: true,
    recursos: [
      "Soluções ilimitadas moderadas",
      "Até 4 automações",
      "Integrações avançadas",
      "Suporte mensal",
      "Gestão de funis",
      "Relatório mensal"
    ]
  },
  {
    nome: "SCALE",
    preco: "R$ 1.490/mês",
    popular: false,
    recursos: [
      "Soluções digitais ilimitadas",
      "Automações ilimitadas",
      "Consultoria tech",
      "Construção de apps/sistemas leves",
      "Evolução contínua",
      "Prioridade total"
    ]
  }
]

export default function Planos() {
  return (
    <section className="py-32 bg-[#0b0b0b]">
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
        <div className="text-center mb-20">
          <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] mb-6">Modelos de parceria.</h2>
          <p className="text-xl text-[#bdbdbd] max-w-3xl mx-auto">Flexíveis, escaláveis e sob medida.</p>
        </div>

        {/* Pricing Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {planos.map((plano, index) => (
            <div
              key={index}
              className={`relative group ${
                plano.popular 
                  ? 'bg-transparent border-2 border-[#1a1a1a]' 
                  : 'bg-transparent border border-[#1a1a1a]'
              } rounded-2xl p-8 hover:border-white/20 transition-all duration-300`}
            >
              {/* Popular badge */}
              {plano.popular && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                  <div className="px-4 py-2 bg-white/90 text-black text-sm font-semibold rounded-full">MAIS POPULAR</div>
                </div>
              )}

              {/* Plan name and price */}
              <div className="text-center mb-8">
                <h3 className="text-2xl font-bold text-[#f2f2f2] mb-2">{plano.nome}</h3>
                <div className="text-3xl font-bold text-[#f2f2f2]">{plano.preco}</div>
              </div>

              {/* Features */}
              <ul className="space-y-4 mb-8">
                {plano.recursos.map((recurso, idx) => (
                  <li key={idx} className="flex items-start gap-3">
                    <svg 
                      className="w-5 h-5 text-white/40 mt-0.5 flex-shrink-0" 
                      fill="none" 
                      stroke="currentColor" 
                      viewBox="0 0 24 24"
                    >
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    <span className="text-[#8c8c8c]">{recurso}</span>
                  </li>
                ))}
              </ul>

              {/* CTA Button */}
              <button className={`w-full py-3 px-6 rounded-lg font-semibold transition-all duration-300 ${
                plano.popular
                  ? 'bg-white text-black hover:bg-white/90'
                  : 'bg-white/10 text-white hover:bg-white/20'
              }`}>
                Começar Agora
              </button>

              {/* Subtle gradient overlay on hover */}
              <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-2xl pointer-events-none" style={{background: "linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0) 100%)"}} />
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
