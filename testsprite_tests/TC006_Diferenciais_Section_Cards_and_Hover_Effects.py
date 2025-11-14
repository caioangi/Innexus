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
        # -> Scroll to the Diferenciais section.
        await page.mouse.wheel(0, 1000)
        

        # -> Scroll down further to locate the Diferenciais section with premium cards or find the section by text and extract its content.
        await page.mouse.wheel(0, 1000)
        

        # -> Hover over the first card in the Diferenciais section to check for the subtle linear hover light effect.
        frame = context.pages[-1]
        # Hover over the first card in the Diferenciais section
        elem = frame.locator('xpath=html/body/div').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Reload the page to observe the initial load animation of the cards and verify if the stagger fade-up animation runs smoothly.
        await page.goto('http://localhost:5173/', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Scroll to the Diferenciais section to observe the stagger fade-up animation on the three premium cards on page load.
        await page.mouse.wheel(0, 1500)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        # Assert the presence of the three premium cards by checking the titles and descriptions from the 'O que criamos.' section
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
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    