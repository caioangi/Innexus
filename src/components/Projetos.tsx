const projetos = [
  {
    titulo: "Sistema de Gestão Empresarial →",
    descricao: "Plataforma completa de gestão interna.",
    slug: "sistema-gestao"
  },
  {
    titulo: "Landing Page Comercial →", 
    descricao: "Página de alta conversão com automação.",
    slug: "landing-comercial"
  },
  {
    titulo: "Dashboard Analytics →",
    descricao: "Painel gerencial com métricas em tempo real.",
    slug: "dashboard-analytics"
  },
  {
    titulo: "Integração WhatsApp →",
    descricao: "Sistema de atendimento automatizado.",
    slug: "integracao-whatsapp"
  },
  {
    titulo: "App de Agendamento →",
    descricao: "Plataforma de reservas e calendário.",
    slug: "app-agendamento"
  }
]

export default function Projetos() {
  return (
    <section className="py-32 bg-[#0b0b0b]">
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
        <div className="text-center mb-20">
          <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] mb-6">Projetos construídos para gerar resultado.</h2>
          <p className="text-xl text-[#bdbdbd]">Clique para ver detalhes de cada projeto.</p>
        </div>

        {/* Projects Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projetos.map((projeto, index) => (
            <a
              key={projeto.slug}
              data-testid={`card-projeto-${projeto.slug}`}
              href={`#projeto-${projeto.slug}`}
              onClick={(e) => {
                e.preventDefault()
                window.location.hash = `projeto-${projeto.slug}`
                console.log(`Projeto clicado: ${projeto.slug}`)
              }}
              className="group relative block p-8 bg-transparent border border-[#1a1a1a] rounded-lg hover:border-white/20 transition-all duration-300"
            >
              {/* Content */}
              <div className="space-y-4">
                <h3 className="text-xl font-semibold text-[#f2f2f2] transition-colors duration-300">
                  {projeto.titulo}
                </h3>
                <p className="text-[#8c8c8c] transition-colors duration-300 leading-relaxed">
                  {projeto.descricao}
                </p>
              </div>
              
              {/* Hover effect - subtle linear glow */}
              <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg pointer-events-none" style={{background: "linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0) 100%)"}} />
            </a>
          ))}
        </div>

        {/* Placeholder anchors for click actions */}
        <div aria-hidden="true" className="sr-only">
          {projetos.map((p) => (
            <span key={p.slug} id={`projeto-${p.slug}`}></span>
          ))}
        </div>
      </div>
    </section>
  )
}
