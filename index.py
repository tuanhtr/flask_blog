from flask import Flask

app = Flask(__name__)



class BB:

    @staticmethod
    def aaa():
        import private

        print(1)




    def test():
        private.__test_function()
        print(1)

if __name__ == '__main__':
    BB.aaa()
    app.run()
