
import aiohttp 

import asyncio

class RequestsIBGE :    

    async def get_html_ibge()-> str:
        
        base_url = 'https://www.ibge.gov.br/explica/codigos-dos-municipios.php'
        
        try:                
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url) as resp:
                    
                    status =  resp.raise_for_status()
                    
                    print(status)
                    
                    html = await resp.text()
                    
                    print(html)
                    
                    return html
                    
        except ValueError as err :            
            print(err)    
                        
            return err

        
    asyncio.run(get_html_ibge())        