from modules.handler import SendMsgToGPT

def main():
    """Функция входа в программу
    """
    message = input("\nВведите ваш запрос: ")
    gpt_sender = SendMsgToGPT()
    response = gpt_sender.send_msg(message)
    print(response)


if __name__ == "__main__":
    hello_text = """Вас приветствует консольное приложение для работы с ChatGPT
Перед началом работы убедитесь что у вас включен VPN"""
    print(hello_text)
    while True:
        main()