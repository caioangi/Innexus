import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None
    
    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()
        
        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )
        
        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)
        
        # Open a new page in the browser context
        page = await context.new_page()
        
        # Navigate to your target URL and wait until the network request is committed
        await page.goto("http://localhost:5173", wait_until="commit", timeout=10000)
        
        # Wait for the main page to reach DOMContentLoaded state (optional for stability)
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
        except async_api.Error:
            pass
        
        # Iterate through all iframes and wait for them to load as well
        for frame in page.frames:
            try:
                await frame.wait_for_load_state("domcontentloaded", timeout=3000)
            except async_api.Error:
                pass
        
        # Interact with the page elements to simulate user flow
        # -> Verify if main titles have font sizes between 48px and 56px and assess visual hierarchy for subheadings and paragraphs.
        await page.mouse.wheel(0, 1000)
        

        # -> Measure the font size of the main title 'Soluções digitais sob medida para acelerar o seu negócio.' visually or by using browser developer tools to confirm if it is between 48px and 56px.
        frame = context.pages[-1]
        # Click 'Agendar Reunião' to check if any style or font size info appears or changes.
        elem = frame.locator('xpath=html/body/div/div/section/div/div[3]/div/a').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Verify that subheadings and paragraph texts follow a clear visual hierarchy consistent with minimalistic design on the landing page.
        await page.mouse.wheel(0, 1000)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        await expect(frame.locator('text=Soluções digitais sob medida para acelerar o seu negócio.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Criamos sites, sistemas, automações e integrações que transformam operações e impulsionam empresas.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Agendar Reunião').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Ver Projetos').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Tecnologia feita sob medida.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Nossa missão é simples: resolver problemas reais através de soluções digitais sob medida. Nada genérico, nada engessado — apenas excelência, precisão e entrega real.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=O que criamos.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Landing pages premium').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Sites institucionais completos').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Web apps e aplicativos internos').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Sistemas sob medida').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Ferramentas personalizadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Automação via N8N').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Integrações com CRM / WhatsApp / APIs').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Dashboards e painéis gerenciais').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Funis digitais e fluxos de vendas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Consultoria tech').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Otimização de processos').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções digitais sob demanda').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Por que escolher a INNEXUS.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Tecnologia de alto nível, criada sob medida para o seu negócio.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções sob medida, sempre').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Nada é genérico ou engessado. Cada projeto nasce de um diagnóstico real e entrega exatamente o que o cliente precisa.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Engenharia + Design + Automação').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Integramos tecnologia, UX e orquestração de processos em soluções completas, inteligentes e eficientes.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Operação digital contínua').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Acompanhamos, ajustamos e evoluímos tudo o que criamos. Sua operação digital nunca para de melhorar.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Como trabalhamos..').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Processo direto, transparente e eficiente.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=1').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Diagnóstico').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Entendimento claro da dor e do objetivo.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=2').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Arquitetura da solução').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Desenhamos a estrutura ideal: páginas, integrações, automações e requisitos técnicos.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=3').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Construção').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Desenvolvimento completo da solução digital, sob medida.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=4').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Refinamento').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Ajustes, melhorias, implementação final.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=5').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Evolução contínua').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Suporte, novas soluções e melhoria contínua.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Projetos construídos para gerar resultado.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Clique para ver detalhes de cada projeto.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Sistema de Gestão Empresarial →').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Plataforma completa de gestão interna.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Landing Page Comercial →').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Página de alta conversão com automação.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Dashboard Analytics →').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Painel gerencial com métricas em tempo real.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Integração WhatsApp →').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Sistema de atendimento automatizado.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=App de Agendamento →').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Plataforma de reservas e calendário.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Modelos de parceria.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Flexíveis, escaláveis e sob medida.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=START').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=R$ 179/mês').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Presença digital básica').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=1 solução por mês').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=1 automação simples').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Suporte técnico').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Entrega inicial 48h').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=MAIS POPULAR').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=GROW').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=R$ 579/mês').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções ilimitadas moderadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Até 4 automações').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Integrações avançadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Suporte mensal').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Gestão de funis').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Relatório mensal').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=SCALE').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=R$ 1.490/mês').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções digitais ilimitadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Automações ilimitadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Consultoria tech').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Construção de apps/sistemas leves').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Evolução contínua').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Prioridade total').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Pronto para construir sua próxima solução digital? Agende uma reunião e receba seu Blueprint INNEXUS.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=INNEXUS').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Boutique de Tecnologia').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções digitais sob demanda').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=© 2024 INNEXUS. Todos os direitos reservados.').first).to_be_visible(timeout=30000)
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    