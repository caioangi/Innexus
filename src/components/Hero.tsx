import React from "react"

type Action = {
  label: string
  href: string
  variant?: "default" | "outline"
}

type HeroProps = {
  className?: string
  title: string
  subtitle?: string
  actions?: Action[]
  titleClassName?: string
  subtitleClassName?: string
  actionsClassName?: string
}

export default function Hero({
  className = "",
  title,
  subtitle,
  actions = [],
  titleClassName = "",
  subtitleClassName = "",
  actionsClassName = "",
}: HeroProps) {
  return (
    <section className={`relative min-h-[70vh] flex items-center justify-center bg-[#0b0b0b] ${className}`}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 className={`text-[#f2f2f2] leading-[1.2] ${titleClassName}`}>{title}</h1>
        {subtitle && (
          <p className={`mt-4 text-[#bdbdbd] mx-auto ${subtitleClassName}`}>{subtitle}</p>
        )}
        {!!actions.length && (
          <div className={`flex flex-col sm:flex-row gap-4 justify-center items-center ${actionsClassName}`}>
            {actions.map((action) => (
              <a
                key={action.label}
                href={action.href}
                className={
                  action.variant === "outline"
                    ? "px-7 py-3 rounded-lg border border-[#1a1a1a] text-[#f2f2f2] hover:border-white/25 transition-all"
                    : "px-7 py-3 rounded-lg bg-white text-black font-semibold hover:bg-white/90 transition-all"
                }
              >
                {action.label}
              </a>
            ))}
          </div>
        )}
      </div>
    </section>
  )
}
