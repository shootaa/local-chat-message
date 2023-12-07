message = input("サーバーに送りたいメッセージを入力してください")

try:
    print("{}というメッセージを送ります".format(message))

    print("サーバーからのメッセージを受け取っています。")
finally:
    print("ソケットを閉じます")