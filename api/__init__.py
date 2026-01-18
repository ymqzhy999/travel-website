# coding:utf-8
import  logging
from flask import Flask, request, session
from .exts import db
from utils.codes import *
from flask.json import JSONEncoder
from datetime import date

# from configs import configs

class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()
 
        return super().default(o)

def create_app(configs):
    app = Flask(__name__,
                  static_url_path='',
                static_folder='templates/front',
                template_folder='assets'
                )
    app.config.from_object((configs['defaultConfig']))
    app.json_encoder = CustomJSONEncoder

    # app.view_functions['static']=login_required(app.send_static_file)

    db.init_app(app)  # 注册数据库

    from api.main import main_bp as main_blueprint
    app.register_blueprint(main_blueprint)


    @app.before_request
    def before_request():
        request__url = request.url.split(request.host, 1)[-1].split('?', 1)[0]
        session['request__url'] = request__url
        # 开始判断当前请求的参数合法性
        try:
            if request.method == 'GET':
                # get使用url拼接，非json
                req_dict = request.args.to_dict()
                try:
                    del req_dict['t']
                except:
                    pass
                session['req_dict'] = req_dict

                instances = req_dict
            elif request.method == 'POST':
                # post时是json数据

                req_dict = request.args.to_dict()
                try:
                    del req_dict['t']
                except:
                    pass
                req_dict2 = request.get_json() if request.get_json() not in [{},[], None] else request.form.to_dict()
                try:
                    req_dict2.update(req_dict)
                except:
                    req_dict2.extend(req_dict)
                print("request.get_json====>", req_dict2)
                session['req_dict'] = req_dict2

        except Exception as e:
            # 错误返回值
            print(Exception, ":", e)
            msg = {
                'code': validate_param_code,
                'message': '本次请求url：{}，参数不规范或有空缺'.format(request__url),
                'data': {}
            }
            logging.warning('{} error :========>{}'.format(request__url, e))
            # return jsonify(msg)

    @app.after_request
    def after_request(response):
        # 请求返回前最后一步，做避免跨域的设置
        response.headers.add('Access-Control-Allow-Origin', '*')
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
        response.headers['Access-Control-Allow-Credentials'] = True
        return response

    return app
