from flask import Flask, request, render_template, redirect


#플라스크 객체 생성
app = Flask(__name__)

#블루 프린트 등록
app.register_blueprint(r.bp)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행