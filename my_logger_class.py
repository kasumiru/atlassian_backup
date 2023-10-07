
class MyLogger():
    @classmethod
    def jprint(self, content):
        try:
            formatted_json = json.dumps(content, indent=4, ensure_ascii=False)
            colorful_json = highlight(
                formatted_json, 
                lexers.JsonLexer(), 
                formatters.Terminal256Formatter()
            )

            print(colorful_json)
        
        except Exception as e:
            print(content)

    @staticmethod
    def print_resp(resp):
        if resp.container.status_code == 200:
            MyLogger.jprint(resp.container.json())
        else:
            print(f'Response code = {resp.container.status_code}')
            try:
                jprint(resp.container.json())
            except Exception as e:
                print(f'MyException: {e}')
                print(f'Response text = {resp.container.text}')

