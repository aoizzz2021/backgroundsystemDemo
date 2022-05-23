import traceback

from django.shortcuts import HttpResponse, render
from django.http import StreamingHttpResponse
import json
import random
import sqlite3
import os
import pymysql
import xlwt

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='ship')
# cursor=pymysql.cursors.DictCursor,是为了将数据作为一个字典返回
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


def login(request):
    username = request.POST['username']
    pwd = request.POST['password']
    sql = 'select * from user where name = "' + str(username) + '" and pwd = "' + str(pwd) + '"'
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    if res != None:
        valid = 1
    else:
        valid = 0
    return HttpResponse(json.dumps({'data': valid}))


def get_data(request):
    sql = 'select * from user '
    cursor.execute(sql)
    res = cursor.fetchall()
    lst = []
    for item in res:
        lst.append(
            {
                "id": item["id"],
                "name": item["name"],
                "pwd": item["pwd"],
                "address": item["address"],
                "state": item["state"],
                "date": item["date"],
                "thumb": item["thumb"]
            }
        )
    data = {
        "list": lst,
        "pageTotal": len(lst)
    }

    return HttpResponse(json.dumps(data))


def del_data(request):
    sql = 'delete from `ship`.`user` where id = ' + str(request.POST['del_id'])
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def insert_data(request):
    temp_dic = request.POST
    name = temp_dic['name']
    pwd = temp_dic['pwd']
    address = temp_dic['address']
    state = '最近登录'
    date = '2022-12-12'
    thumb = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fup.enterdesk.com%2Fedpic_360_360%2Ff5%2F7f%2F6d%2Ff57f6de506033a00909f2307f6e2021f.jpg&refer=http%3A%2F%2Fup.enterdesk.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1655015346&t=0e167ef862f6fd617649a3d8f6abdd2dg"
    sql = 'select max(id) from `ship`.`user` '
    cursor.execute(sql)
    res = cursor.fetchone()
    id = res['max(id)']
    if id:
        id += 1
    else:
        id = 1
    sql = 'INSERT INTO `ship`.`user` (`id`, `name`, `pwd`, `address`, `state`, `date`, `thumb`) VALUES (' + str(
        id) + ',"' + str(name) + '","' + str(pwd) + '","' + str(address) + '","' + str(state) + '","' + str(
        date) + '","' + str(thumb) + '")'
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('提交成功！'))


def post_invis_data(request):
    ship_id = request.POST['id']
    sql = 'select bw,over_count,normal_count,danger_count,cold_count from `ship`.`inportinfo` where ship_id = ' + str(
        ship_id) + ' order by bw desc'
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "info": res
    }

    return HttpResponse(json.dumps(data))


def post_outvis_data(request):
    ship_id = request.POST['id']
    sql = 'select bw,over_count,normal_count,danger_count,cold_count from `ship`.`outportinfo` where ship_id = ' + str(
        ship_id) + ' order by bw desc'
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "info": res
    }

    return HttpResponse(json.dumps(data))


def set_insch_data(request):
    temp_dic = request.POST
    tabledata = json.loads(temp_dic['tabledata'])
    ship_id = temp_dic['ship_id']
    sql = 'delete from `ship`.`insce` where ship_id = ' + str(ship_id)
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    inp = temp_dic['inp']
    incount = temp_dic['incount']
    outp = temp_dic['outp']
    count = temp_dic['count']
    date = temp_dic['date']
    sql = 'select max(id) from `ship`.`insce` '
    cursor.execute(sql)
    res = cursor.fetchone()
    id = res['max(id)']
    if id:
        id += 1
    else:
        id = 1
    for i in range(len(tabledata)):
        sql = 'INSERT INTO `ship`.`insce` (`id`, `ship_id`, `bw`, `ph`, `st`, `ht`, `zsc`, `jjb`, `kcg`, `tgcf`, `cxx`, `jczh`, `wgsd`, `count`) VALUES (' + str(
            id) + ', ' + str(
            ship_id) + ', ' + str(tabledata[i]['bw']) + ', ' + str(tabledata[i]['ph']) + ', "' + str(
            tabledata[i]['st']) + '", ' + str(
            tabledata[i]['ht']) + ', ' + str(tabledata[i]['zsc']) + ', ' + str(
            tabledata[i]['jjb']) + ', ' + str(tabledata[i]['kcg']) + ', ' + str(tabledata[i]['tgcf']) + ', ' + str(
            tabledata[i]['cxx']) + ', ' + str(tabledata[i]['jczh']) + ', "' + str(tabledata[i]['wgsd']) + '", ' + str(
            incount) + ')'
        print(sql)
        id += 1
        cursor.execute(sql)
        conn.commit()
    return HttpResponse(json.dumps('提交成功！'))


def post_insce_data(request):
    ship_id = request.POST['id']
    sql = 'select * from `ship`.`insce` where ship_id = ' + str(ship_id)
    cursor.execute(sql)
    res = cursor.fetchall()

    data = {
        "res": res
    }
    return HttpResponse(json.dumps(data))


def del_insce_data(request):
    sql = 'delete from `ship`.`insce` where id = ' + str(request.POST['del_id'])
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def set_outsch_data(request):
    temp_dic = request.POST
    tabledata = json.loads(temp_dic['tabledata'])
    ship_id = temp_dic['ship_id']
    sql = 'delete from `ship`.`outsce` where ship_id = ' + str(ship_id)
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    inp = temp_dic['inp']
    incount = temp_dic['incount']
    outp = temp_dic['outp']
    count = temp_dic['count']
    date = temp_dic['date']
    sql = 'select max(id) from `ship`.`outsce` '
    cursor.execute(sql)
    res = cursor.fetchone()
    id = res['max(id)']
    if id:
        id += 1
    else:
        id = 1
    for i in range(len(tabledata)):
        sql = 'INSERT INTO `ship`.`outsce` (`id`, `ship_id`, `bw`, `ph`, `st`, `ht`, `zsc`, `jjb`, `kcg`, `tgcf`, `cxx`, `jczh`, `wgsd`, `count`) VALUES (' + str(
            id) + ', ' + str(
            ship_id) + ', ' + str(tabledata[i]['bw']) + ', ' + str(tabledata[i]['ph']) + ', "' + str(
            tabledata[i]['st']) + '", ' + str(
            tabledata[i]['ht']) + ', ' + str(tabledata[i]['zsc']) + ', ' + str(
            tabledata[i]['jjb']) + ', ' + str(tabledata[i]['kcg']) + ', ' + str(tabledata[i]['tgcf']) + ', ' + str(
            tabledata[i]['cxx']) + ', ' + str(tabledata[i]['jczh']) + ', "' + str(tabledata[i]['wgsd']) + '", ' + str(
            incount) + ')'
        id += 1
        cursor.execute(sql)
        conn.commit()
    return HttpResponse(json.dumps('提交成功！'))


def post_outsce_data(request):
    ship_id = request.POST['id']
    sql = 'select * from `ship`.`outsce` where ship_id = ' + str(ship_id)
    cursor.execute(sql)
    res = cursor.fetchall()

    data = {
        "res": res
    }
    return HttpResponse(json.dumps(data))


def del_outsce_data(request):
    sql = 'delete from `ship`.`outsce` where id = ' + str(request.POST['del_id'])
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def post_plan_data(request):
    ship_id = request.POST['id']
    sql = 'select * from `ship`.`outsce` where ship_id = ' + str(ship_id)
    cursor.execute(sql)
    out_res = cursor.fetchall()
    sql = 'select * from `ship`.`insce` where ship_id = ' + str(ship_id)
    cursor.execute(sql)
    in_res = cursor.fetchall()
    templst = []
    id = 0
    for i in range(len(in_res)):
        id += 1
        templst.append({
            'id': id,
            'bw': in_res[i]['bw'],
            'incount': in_res[i]['count'],
            'inkcg': in_res[i]['kcg'],
            'incxx': in_res[i]['cxx'],
            'inzsc': in_res[i]['zsc'],
            'outcount': out_res[i]['count'],
            'outkcg': out_res[i]['kcg'],
            'outcxx': out_res[i]['cxx'],
            'outzsc': out_res[i]['zsc'],
            'allcount': in_res[i]['count'] + out_res[i]['count'],
            'zsc': in_res[i]['zsc'] + out_res[i]['zsc'],
            'eff': (in_res[i]['count'] + out_res[i]['count']) / (in_res[i]['zsc'] + out_res[i]['zsc']),
        })
    data = {
        "res": templst
    }
    return HttpResponse(json.dumps(data))


def get_ship_data(request):
    sql = 'select * from `ship`.`shipdata` '
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "list": res,
        "pageTotal": len(res),
    }

    return HttpResponse(json.dumps(data))


def post_ship_data(request):
    ship_id = request.POST['id']
    sql = 'select * from `ship`.`inportinfo` where ship_id = ' + str(ship_id)
    cursor.execute(sql)
    in_res = cursor.fetchall()

    sql = 'select * from `ship`.`outportinfo` where ship_id = ' + str(ship_id)
    cursor.execute(sql)
    out_res = cursor.fetchall()
    # id = res['max(id)']
    data = {
        "in_res": in_res,
        'out_res': out_res
    }
    return HttpResponse(json.dumps(data))


def get_shipname(request):
    sql = 'select id,ship_name from `ship`.`shipdata` '
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    # print(res)
    data = {
        'list': res
    }

    return HttpResponse(json.dumps(data))


def del_ship_data(request):
    sql = 'delete from `ship`.`shipdata` where id = ' + str(request.POST['del_id'])
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def insert_ship_data(request):
    temp_dic = request.POST
    sql = 'select max(id) from `ship`.`shipdata` '
    cursor.execute(sql)
    res = cursor.fetchone()
    id = res['max(id)']
    if id:
        id += 1
    else:
        id = 1
    sql = 'INSERT INTO `ship`.`shipdata` VALUES (' + str(temp_dic['id']) + ',"' + str(
        temp_dic['ship_name']) + '",' + str(temp_dic['ship_len']) + ',' + str(temp_dic['ship_width']) + ',' + str(
        temp_dic['ship_maxcase']) + ',' + str(
        temp_dic['ship_dwt']) + ',' + str(temp_dic['ship_depth']) + ',' + str(temp_dic['ship_sw']) + ',' + str(
        temp_dic['ship_cbh']) + ',' + str(temp_dic['ship_hbh']) + ',' + str(temp_dic['ship_rlh']) + ',' + str(
        temp_dic['ship_dl']) + ',' + str(temp_dic['ship_hl']) + ',' + str(temp_dic['ship_al']) + ',' + str(
        temp_dic['ship_we']) + ',' + str(temp_dic['ship_idh']) + ',' + str(temp_dic['ship_idr']) + ',' + str(
        temp_dic['ship_idm']) + ',' + str(temp_dic['ship_th']) + ',' + str(temp_dic['ship_afhc']) + ',"' + str(
        temp_dic['ship_afhh']) + '",' + str(temp_dic['ship_wh']) + ',' + str(temp_dic['ship_ihmin']) + ',' + str(
        temp_dic['ship_ihmax']) + ')'
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('新增成功'))


def post_inbei_data(request):
    id = request.POST['id']
    sql = 'select id,bw,over_count,normal_count,cold_count,danger_count,all_count from `ship`.`inportinfo` where ship_id = ' + str(
        id)
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "list": res,
        "pageTotal": len(res),
    }

    return HttpResponse(json.dumps(data))


def del_inbei_data(request):
    sql = 'delete from `ship`.`inportinfo` where id = ' + str(request.POST['del_id'])
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def insert_inbei_data(request):
    temp_dic = request.POST
    sql = 'select max(id) from `ship`.`inportinfo` '
    cursor.execute(sql)
    res = cursor.fetchone()
    ship_id = temp_dic['ship_id']
    id = res['max(id)']
    if id:
        id += 1
    else:
        id = 1
    sql = 'INSERT INTO `ship`.`inportinfo` (`id`, `bw`, `col`, `layer`, `over_count`, `normal_count`, `cold_count`, `danger_count`, `all_count`, `ship_id`) VALUES (' + str(
        id) + ', ' + str(temp_dic['name']) + ', ' + str(0) + ', ' + str(0) + ', ' + str(
        temp_dic['over_count']) + ', ' + str(temp_dic['normal_count']) + ', ' + str(
        temp_dic['cold_count']) + ', ' + str(temp_dic['danger_count']) + ', ' + str(temp_dic['all_count']) + ', ' + str(
        ship_id) + ')'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('新增成功'))


def post_outbei_data(request):
    id = request.POST['id']
    sql = 'select id,bw,over_count,normal_count,cold_count,danger_count,all_count from `ship`.`outportinfo` where ship_id = ' + str(
        id)
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "list": res,
        "pageTotal": len(res),
    }

    return HttpResponse(json.dumps(data))


def del_outbei_data(request):
    sql = 'delete from `ship`.`outportinfo` where id = ' + str(request.POST['del_id'])
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def insert_outbei_data(request):
    temp_dic = request.POST
    sql = 'select max(id) from `ship`.`outportinfo` '
    cursor.execute(sql)
    res = cursor.fetchone()
    ship_id = temp_dic['ship_id']
    id = res['max(id)']
    if id:
        id += 1
    else:
        id = 1
    sql = 'INSERT INTO `ship`.`outportinfo` (`id`, `bw`, `col`, `layer`, `over_count`, `normal_count`, `cold_count`, `danger_count`, `all_count`, `ship_id`) VALUES (' + str(
        id) + ', ' + str(temp_dic['name']) + ', ' + str(0) + ', ' + str(0) + ', ' + str(
        temp_dic['over_count']) + ', ' + str(temp_dic['normal_count']) + ', ' + str(
        temp_dic['cold_count']) + ', ' + str(temp_dic['danger_count']) + ', ' + str(temp_dic['all_count']) + ', ' + str(
        ship_id) + ')'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('新增成功'))


def get_cargo_data(request):
    sql = 'select * from `ship`.`cargodata` '
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "list": res,
        "pageTotal": len(res),
    }

    return HttpResponse(json.dumps(data))


def post_incargo_data(request):
    id = request.POST['id']
    sql = 'select id,bw,col,layer,over_count,normal_count,cold_count,danger_count from `ship`.`inportinfo` where ship_id = ' + str(
        id)
    cursor.execute(sql)
    res = cursor.fetchall()
    temp = []
    for item in res:
        cargo_type = ''
        if item['over_count'] == 1:
            cargo_type = '超限箱'
        if item['normal_count'] == 1:
            cargo_type = '普通箱'
        if item['cold_count'] == 1:
            cargo_type = '冷藏箱'
        if item['danger_count'] == 1:
            cargo_type = '危险箱'
        temp.append(
            {'id': item['id'], 'name': item['bw'], 'col': item['col'], 'layer': item['layer'], 'type': cargo_type})
    data = {
        "list": temp,
        "pageTotal": len(temp),
    }

    return HttpResponse(json.dumps(data))


def del_incargo_data(request):
    sql = 'delete from `ship`.`inportinfo` where id = ' + str(request.POST['del_id'])
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def insert_incargo_data(request):
    temp_dic = request.POST
    cargo_type = request.POST['type']
    over_count = '0'
    danger_count = '0'
    normal_count = '0'
    cold_count = '0'
    print(cargo_type)
    if cargo_type == '0':
        over_count = '1'
    if cargo_type == '1':
        danger_count = '1'
    if cargo_type == '2':
        normal_count = '1'
    if cargo_type == '3':
        cold_count = '1'

    sql = 'select max(id) from `ship`.`inportinfo` '
    cursor.execute(sql)
    res = cursor.fetchone()
    id = res['max(id)']
    ship_id = temp_dic['ship_id']
    if id:
        id += 1
    else:
        id = 1
    sql = 'INSERT INTO `ship`.`inportinfo` (`id`, `bw`, `col`, `layer`, `over_count`, `normal_count`, `cold_count`, `danger_count`, `all_count`, `ship_id`) VALUES (' + str(
        id) + ', ' + str(temp_dic['name']) + ', ' + str(temp_dic['col']) + ', ' + str(temp_dic[
                                                                                          'layer']) + ', ' + over_count + ', ' + normal_count + ', ' + cold_count + ', ' + danger_count + ', ' + '1' + ', ' + str(
        ship_id) + ')'
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('新增成功'))


def post_outcargo_data(request):
    id = request.POST['id']
    sql = 'select id,bw,col,layer,over_count,normal_count,cold_count,danger_count from `ship`.`outportinfo` where ship_id = ' + str(
        id)
    cursor.execute(sql)
    res = cursor.fetchall()
    temp = []
    for item in res:
        cargo_type = ''
        if item['over_count'] == 1:
            cargo_type = '超限箱'
        if item['normal_count'] == 1:
            cargo_type = '普通箱'
        if item['cold_count'] == 1:
            cargo_type = '冷藏箱'
        if item['danger_count'] == 1:
            cargo_type = '危险箱'
        temp.append(
            {'id': item['id'], 'name': item['bw'], 'col': item['col'], 'layer': item['layer'], 'type': cargo_type})
    data = {
        "list": temp,
        "pageTotal": len(temp),
    }

    return HttpResponse(json.dumps(data))


def del_outcargo_data(request):
    sql = 'delete from `ship`.`outportinfo` where id = ' + str(request.POST['del_id'])
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('删除成功'))


def insert_outcargo_data(request):
    temp_dic = request.POST
    cargo_type = request.POST['type']
    over_count = '0'
    danger_count = '0'
    normal_count = '0'
    cold_count = '0'
    print(cargo_type)
    if cargo_type == '0':
        over_count = '1'
    if cargo_type == '1':
        danger_count = '1'
    if cargo_type == '2':
        normal_count = '1'
    if cargo_type == '3':
        cold_count = '1'

    sql = 'select max(id) from `ship`.`outportinfo` '
    cursor.execute(sql)
    res = cursor.fetchone()
    id = res['max(id)']
    ship_id = temp_dic['ship_id']
    if id:
        id += 1
    else:
        id = 1
    sql = 'INSERT INTO `ship`.`outportinfo` (`id`, `bw`, `col`, `layer`, `over_count`, `normal_count`, `cold_count`, `danger_count`, `all_count`, `ship_id`) VALUES (' + str(
        id) + ', ' + str(temp_dic['name']) + ', ' + str(temp_dic['col']) + ', ' + str(temp_dic[
                                                                                          'layer']) + ', ' + over_count + ', ' + normal_count + ', ' + cold_count + ', ' + danger_count + ', ' + '1' + ', ' + str(
        ship_id) + ')'
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(json.dumps('新增成功'))


def get_in_file(request):
    """接收文件"""
    try:
        ship_id = request.POST['id']
        sql = 'delete from `ship`.`inportinfo` where ship_id = ' + str(ship_id)
        cursor.execute(sql)
        conn.commit()
        files = request.FILES.getlist("file", None)  # 接收前端传递过来的多个文件
        for file in files:
            # 写入文件
            with open('temp.txt', 'wb') as f:
                for content in file.chunks():
                    f.write(content)
        lst = []
        with open('temp.txt', 'r') as f:
            lst = f.readlines()
        data_dic = {}
        for item in lst:
            if item.startswith('LOC+147'):
                bw = item[8:11]
                col = item[11:13]
                layer = item[13:15]
                cold_count = 0
                danger_count = 0
                over_count = 0
                normal_count = 1
                data_dic[bw] = {'col': 0, 'layer': 0, 'over_count': 0, 'normal_count': 1, 'cold_count': 0,
                                'danger_count': 0}
                data_dic[bw]['col'] = col
                data_dic[bw]['layer'] = layer
            else:
                if item.startswith('TMP'):
                    cold_count = 1
                    data_dic[bw]['normal_count'] = 0
                    data_dic[bw]['cold_count'] = cold_count
                elif item.startswith('DIM'):
                    over_count = 1
                    data_dic[bw]['normal_count'] = 0
                    data_dic[bw]['over_count'] = over_count
                elif item.startswith('DSG'):
                    danger_count = 1
                    data_dic[bw]['normal_count'] = 0
                    data_dic[bw]['danger_count'] = danger_count
                # else:
                #     normal_count += 1
                #     data_dic[bw]['normal_count'] = normal_count
        sql = 'select max(id) from `ship`.`inportinfo` '
        cursor.execute(sql)
        res = cursor.fetchone()
        id = res['max(id)']
        try:
            for key in data_dic.keys():
                if id:
                    id += 1
                else:
                    id = 1
                sql = 'INSERT INTO `ship`.`inportinfo` (`id`, `bw`, `col`, `layer`, `over_count`, `normal_count`, `cold_count`, `danger_count`, `all_count`, `ship_id`) VALUES (' + str(
                    id) + ', ' + str(key) + ', ' + str(data_dic[key]['col']) + ', ' + str(
                    data_dic[key]['layer']) + ', ' + str(data_dic[key]['over_count']) + ', ' + str(
                    data_dic[key]['normal_count']) + ', ' + str(data_dic[key]['cold_count']) + ', ' + str(
                    data_dic[key]['danger_count']) + ', ' + str((data_dic[key]['over_count'] + data_dic[key][
                    'normal_count'] + data_dic[key]['cold_count'] + data_dic[key]['danger_count'])) + ', ' + str(
                    ship_id) + ')'
                cursor.execute(sql)
                conn.commit()
        except:
            print(traceback.format_exc())
            print(sql)
        return HttpResponse(data_dic)
    except Exception as e:
        return HttpResponse(code=401, msg=str(e))


def get_out_file(request):
    """接收文件"""
    try:
        ship_id = request.POST['id']
        sql = 'delete from `ship`.`outportinfo` where ship_id = ' + str(ship_id)
        cursor.execute(sql)
        conn.commit()
        files = request.FILES.getlist("file", None)  # 接收前端传递过来的多个文件
        for file in files:
            # 写入文件
            with open('temp.txt', 'wb') as f:
                for content in file.chunks():
                    f.write(content)
        lst = []
        with open('temp.txt', 'r') as f:
            lst = f.readlines()
        data_dic = {}
        for item in lst:
            if item.startswith('LOC+147'):
                bw = item[8:11]
                col = item[11:13]
                layer = item[13:15]
                cold_count = 0
                danger_count = 0
                over_count = 0
                normal_count = 1
                data_dic[bw] = {'col': 0, 'layer': 0, 'over_count': 0, 'normal_count': 1, 'cold_count': 0,
                                'danger_count': 0}
                data_dic[bw]['col'] = col
                data_dic[bw]['layer'] = layer
            else:
                if item.startswith('TMP'):
                    cold_count = 1
                    data_dic[bw]['normal_count'] = 0
                    data_dic[bw]['cold_count'] = cold_count
                elif item.startswith('DIM'):
                    over_count = 1
                    data_dic[bw]['normal_count'] = 0
                    data_dic[bw]['over_count'] = over_count
                elif item.startswith('DSG'):
                    danger_count = 1
                    data_dic[bw]['normal_count'] = 0
                    data_dic[bw]['danger_count'] = danger_count
                # else:
                #     normal_count += 1
                #     data_dic[bw]['normal_count'] = normal_count
        sql = 'select max(id) from `ship`.`outportinfo` '
        cursor.execute(sql)
        res = cursor.fetchone()
        id = res['max(id)']
        try:
            for key in data_dic.keys():
                if id:
                    id += 1
                else:
                    id = 1
                sql = 'INSERT INTO `ship`.`outportinfo` (`id`, `bw`, `col`, `layer`, `over_count`, `normal_count`, `cold_count`, `danger_count`, `all_count`, `ship_id`) VALUES (' + str(
                    id) + ', ' + str(key) + ', ' + str(data_dic[key]['col']) + ', ' + str(
                    data_dic[key]['layer']) + ', ' + str(data_dic[key]['over_count']) + ', ' + str(
                    data_dic[key]['normal_count']) + ', ' + str(data_dic[key]['cold_count']) + ', ' + str(
                    data_dic[key]['danger_count']) + ', ' + str((data_dic[key]['over_count'] + data_dic[key][
                    'normal_count'] + data_dic[key]['cold_count'] + data_dic[key]['danger_count'])) + ', ' + str(
                    ship_id) + ')'
                cursor.execute(sql)
                conn.commit()
        except:
            print(traceback.format_exc())
            print(sql)
        return HttpResponse(data_dic)
    except Exception as e:
        return HttpResponse(code=401, msg=str(e))


def export_file_data(request):
    try:
        ship_id = request.POST['ship_id']
        sql = 'select * from `ship`.`inportinfo` where ship_id = '+str(ship_id)+' order by bw'
        cursor.execute(sql)
        in_res = cursor.fetchall()
        # id = res['max(id)']
        os.remove(os.path.join(os.getcwd(),'xls','在港作业信息.xls'))
        wb = xlwt.Workbook(encoding='utf-8')
        sht = wb.add_sheet('在港作业信息')
        sht.write(0, 0, '进口')
        sht.write(1, 0, '贝位')
        sht.write(1, 1, '列')
        sht.write(1, 2, '层数')
        sht.write(1, 3, '超限箱')
        sht.write(1, 4, '普通箱')
        sht.write(1, 5, '冷藏箱')
        sht.write(1, 6, '危险箱')
        sht.write(1, 7, '总箱数')
        row = 2
        for item in in_res:
            sht.write(row, 0, item['bw'])
            sht.write(row, 1, item['col'])
            sht.write(row, 2, item['layer'])
            sht.write(row, 3, item['over_count'])
            sht.write(row, 4, item['normal_count'])
            sht.write(row, 5, item['cold_count'])
            sht.write(row, 6, item['danger_count'])
            sht.write(row, 7, item['all_count'])
            row += 1
        sql = 'select * from `ship`.`outportinfo` where ship_id = '+str(ship_id)+' order by bw'
        cursor.execute(sql)
        out_res = cursor.fetchall()
        sht.write(row, 0, '出口')
        row +=1
        sht.write(row, 0, '贝位')
        sht.write(row, 1, '列')
        sht.write(row, 2, '层数')
        sht.write(row, 3, '超限箱')
        sht.write(row, 4, '普通箱')
        sht.write(row, 5, '冷藏箱')
        sht.write(row, 6, '危险箱')
        sht.write(row, 7, '总箱数')
        row += 1
        for item in out_res:
            sht.write(row, 0, item['bw'])
            sht.write(row, 1, item['col'])
            sht.write(row, 2, item['layer'])
            sht.write(row, 3, item['over_count'])
            sht.write(row, 4, item['normal_count'])
            sht.write(row, 5, item['cold_count'])
            sht.write(row, 6, item['danger_count'])
            sht.write(row, 7, item['all_count'])
            row += 1
        wb.save(os.path.join(os.getcwd(),'xls','在港作业信息.xls'))
        file_path = os.path.join(os.getcwd(),'xls','在港作业信息.xls')
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception as e:
        return HttpResponse(code=401, msg=str(e))

def export_plan_data(request):
    try:
        ship_id = request.POST['ship_id']
        sql = 'select * from `ship`.`insce` where ship_id = '+str(ship_id)+' order by bw'
        cursor.execute(sql)
        in_res = cursor.fetchall()
        # id = res['max(id)']
        try:
            os.remove(os.path.join(os.getcwd(),'xls','作业信息编制.xls'))
        except:
            pass
        wb = xlwt.Workbook(encoding='utf-8')
        sht = wb.add_sheet('作业信息编制')

        sql = 'select * from `ship`.`outsce` where ship_id = '+str(ship_id)+' order by bw'
        cursor.execute(sql)
        out_res = cursor.fetchall()
        sht.write(1, 0, '岸桥')
        sht.write(1, 1, '进口')
        sht.write(1, 2, '出口')
        sht.write(1, 3, '总钩')
        sht.write(1, 4, '开舱盖')
        sht.write(1, 5, '卸超限')
        sht.write(1, 6, '关舱盖')
        sht.write(1, 7, '装超限')
        sht.write(1, 8, '总时')
        sht.write(1, 9, '计划效率')
        row = 2
        for i in range(len(in_res)):
            sht.write(row, 0, in_res[i]['bw'])
            sht.write(row, 1, in_res[i]['count'])
            sht.write(row, 2, out_res[i]['count'])
            sht.write(row, 3, in_res[i]['count'] + out_res[i]['count'])
            sht.write(row, 4, in_res[i]['kcg'])
            sht.write(row, 5, in_res[i]['cxx'])
            sht.write(row, 6, out_res[i]['kcg'])
            sht.write(row, 7, out_res[i]['cxx'])
            sht.write(row, 8, in_res[i]['zsc'] + out_res[i]['zsc'])
            sht.write(row, 9, (in_res[i]['count'] + out_res[i]['count']) / (in_res[i]['zsc'] + out_res[i]['zsc']))
            row += 1

        wb.save(os.path.join(os.getcwd(),'xls','作业信息编制.xls'))
        file_path = os.path.join(os.getcwd(),'xls','作业信息编制.xls')
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception as e:
        return HttpResponse(code=401, msg=str(e))


def get_in_file_data(request):
    try:
        sql = 'select * from `ship`.`inportinfo` '
        cursor.execute(sql)
        res = cursor.fetchall()
        # id = res['max(id)']
        data = {
            "list": res,
        }
        return HttpResponse(json.dumps(data))
    except Exception as e:
        return HttpResponse(code=401, msg=str(e))


def get_out_file_data(request):
    try:
        sql = 'select * from `ship`.`outportinfo` '
        cursor.execute(sql)
        res = cursor.fetchall()
        # id = res['max(id)']
        data = {
            "list": res,
        }
        return HttpResponse(json.dumps(data))
    except Exception as e:
        return HttpResponse(code=401, msg=str(e))
