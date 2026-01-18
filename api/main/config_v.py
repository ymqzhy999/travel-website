# coding:utf-8
__author__ = "ila"

import logging
from flask import request, jsonify, session

from api.models.config_model import config
from . import main_bp
from utils.codes import *
from utils import message as mes


@main_bp.route("/python1s2c1/config/page", methods=['GET'])
def python1s2c1_config_page():
    '''
    获取参数信息
    :return:
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {"currPage": 1, "totalPage": 1, "total": 1, "pageSize": 10, "list": []}}
        req_dict = session.get('req_dict')
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize'] = config.page(config, config, req_dict)
        return jsonify(msg)

@main_bp.route("/python1s2c1/config/list", methods=['GET'])
def python1s2c1_config_list():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = config.page(config, config, req_dict)

        return jsonify(msg)


@main_bp.route("/python1s2c1/config/info/<id>", methods=['GET'])
def python1s2c1_config_info(id):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data = config.getbyid(config, config, int(id))
        if len(data)>0:
            msg['data'] =data[0]
        return jsonify(msg)


@main_bp.route("/python1s2c1/config/detail/<id>", methods=['GET'])
def python1s2c1_config_detail(id):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data =config.getbyid(config, config, int(id))
        if len(data)>0:
            msg['data']=data[0]
        return jsonify(msg)



@main_bp.route("/python1s2c1/config/save", methods=['POST'])
def python1s2c1_config_save():
    '''
    创建参数信息
    :return:
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        req_dict = session.get('req_dict')
        param1 = config.getbyparams(config, config, req_dict)
        if param1:
            msg['code'] = id_exist_code
            msg['msg'] = mes.id_exist_code
            return jsonify(msg)

        error = config.createbyreq(config, config, req_dict)
        logging.warning("save_config.res=========>{}".format(error))
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)


@main_bp.route("/python1s2c1/config/add", methods=['POST'])
def python1s2c1_config_add():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")

        error=config.createbyreq(config, config, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)
        

@main_bp.route("/python1s2c1/config/update", methods=['POST'])
def python1s2c1_config_update():
    '''
    更新参数信息
    :return:
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        req_dict = session.get('req_dict')

        config.updatebyparams(config, config, req_dict)

        return jsonify(msg)


@main_bp.route("/python1s2c1/config/delete", methods=['POST'])
def python1s2c1_config_delete():
    '''
    删除参数信息
    :return:
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        req_dict = session.get('req_dict')
        config.delete(
            config,
            req_dict
        )

        return jsonify(msg)
