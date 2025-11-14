export default function CTA() {
  return (
    <section className="py-32 bg-[#0b0b0b]">
      <div className="max-w-4xl mx-auto px-6 lg:px-8 text-center">
        <h2 className="text-4xl md:text-5xl font-bold text-[#f2f2f2] mb-6">Pronto para construir sua próxima solução digital?</h2>
        <p className="text-xl text-[#bdbdbd] mb-12 max-w-2xl mx-auto">Agende uma reunião e receba seu Blueprint INNEXUS.</p>
        
        {/* CTA Button */}
        <button
          data-testid="cta-agendar"
          onClick={() => {
            console.log("CTA: Agendar Reunião")
            window.location.hash = "agenda"
          }}
          className="group relative px-8 py-4 bg-white text-black font-semibold rounded-lg hover:bg-white/90 transition-all duration-300"
        >
          <span className="relative z-10">Agendar Reunião</span>
          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        </button>

        {/* Placeholder anchor for CTA */}
        <span id="agenda" aria-hidden="true" className="sr-only"></span>
      </div>
    </section>
  )
}
