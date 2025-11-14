import { Hero } from "@/components/blocks/hero"
import Posicionamento from "@/components/Posicionamento"
import OQueCriamos from "@/components/OQueCriamos"
import Diferenciais from "@/components/Diferenciais"
import Processo from "@/components/Processo"
import Projetos from "@/components/Projetos"
import Planos from "@/components/Planos"
import CTA from "@/components/CTA"
import Footer from "@/components/Footer"

export default function Home() {
  return (
    <div className="min-h-screen bg-[#0b0b0b] text-white">
      <Hero
        title="Soluções digitais sob medida para acelerar o seu negócio."
        subtitle="Criamos sites, sistemas, automações e integrações que transformam operações e impulsionam empresas."
        actions={[
          { label: "Agendar Reunião", href: "#", variant: "default" },
          { label: "Ver Projetos", href: "#", variant: "outline" },
        ]}
        titleClassName="text-5xl md:text-[56px] font-extrabold leading-[1.2]"
        subtitleClassName="text-lg md:text-xl max-w-[650px] text-white/70"
        actionsClassName="mt-8"
      />
      <Posicionamento />
      <OQueCriamos />
      <Diferenciais />
      <Processo />
      <Projetos />
      <Planos />
      <CTA />
      <Footer />
    </div>
  )
}
