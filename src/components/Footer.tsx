export default function Footer() {
  return (
    <footer className="py-16 bg-[#0b0b0b] border-t border-[#1a1a1a]">
      <div className="max-w-6xl mx-auto px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center gap-8">
          {/* Logo/Brand */}
          <div className="text-center md:text-left">
            <h3 className="text-2xl font-bold text-[#f2f2f2] mb-2">
              INNEXUS
            </h3>
            <p className="text-[#8c8c8c]">Boutique de Tecnologia</p>
          </div>
          
          {/* Contact */}
          <div className="text-center md:text-right">
            <p className="text-[#8c8c8c] mb-2">
              Soluções digitais sob demanda
            </p>
            <p className="text-[#8c8c8c] text-sm">
              © 2024 INNEXUS. Todos os direitos reservados.
            </p>
          </div>
        </div>
      </div>
    </footer>
  )
}
