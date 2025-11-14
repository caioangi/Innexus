const processos = [
  {
    numero: "1",
    titulo: "Diagnóstico",
    descricao: "Entendimento claro da dor e do objetivo."
  },
  {
    numero: "2", 
    titulo: "Arquitetura da solução",
    descricao: "Desenhamos a estrutura ideal: páginas, integrações, automações e requisitos técnicos."
  },
  {
    numero: "3",
    titulo: "Construção", 
    descricao: "Desenvolvimento completo da solução digital, sob medida."
  },
  {
    numero: "4",
    titulo: "Refinamento",
    descricao: "Ajustes, melhorias, implementação final."
  },
  {
    numero: "5",
    titulo: "Evolução contínua",
    descricao: "Suporte, novas soluções e melhoria contínua."
  }
]

export default function Processo() {
  return (
    <section className="py-32 bg-[#0b0b0b]">
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
        <div className="text-center mb-20">
          <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] mb-6">Como trabalhamos..</h2>
          <p className="text-xl text-[#bdbdbd] max-w-3xl mx-auto">Processo direto, transparente e eficiente.</p>
        </div>

        {/* Process steps */}
        <div className="max-w-4xl mx-auto">
          {processos.map((processo, index) => (
            <div key={index} className="group relative mb-16 last:mb-0">
              <div className="flex items-start gap-8">
                {/* Floating large number */}
                <div className="flex-shrink-0">
                  <div className="text-6xl md:text-8xl font-bold text-white/5 group-hover:text-white/10 transition-colors duration-300">
                    {processo.numero}
                  </div>
                </div>
                
                <div className="flex-1 pt-4">
                  <h3 className="text-2xl md:text-3xl font-semibold text-[#f2f2f2] mb-3">{processo.titulo}</h3>
                  <p className="text-lg text-[#8c8c8c] leading-relaxed">{processo.descricao}</p>
                </div>
              </div>
              
              {/* Subtle connector line */}
              {index < processos.length - 1 && (
                <div className="absolute left-16 top-24 bottom-0 w-px bg-[#1a1a1a] transition-colors duration-300" />
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
