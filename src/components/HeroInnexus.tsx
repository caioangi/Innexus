import { Hero } from "@/components/blocks/hero"

function HeroInnexus() {
  return (
    <Hero
      title="Soluções digitais sob medida para acelerar o seu negócio."
      subtitle="Criamos sites, sistemas, automações e integrações que transformam operações e impulsionam empresas."
      actions={[
        {
          label: "Agendar Reunião",
          href: "#",
          variant: "default"
        },
        {
          label: "Ver Projetos",
          href: "#",
          variant: "outline"
        }
      ]}
      titleClassName="text-5xl md:text-6xl font-extrabold"
      subtitleClassName="text-lg md:text-xl max-w-[650px] text-white/70"
      actionsClassName="mt-8"
    />
  );
}

export { HeroInnexus }
