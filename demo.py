import os
import numpy as np
from boxplot import BoxPlot
from curve_vis import CurveVis
from icecream import install
install()



def eval_sim(model_list=['6dof', '2dof']):
    b = BoxPlot('Error','model', 'm/rad')
    # show_datas = [[],[],[],[],[],[]]
    show_datas = [[],[]]
    # x_indexs = ['mean', '']
    data_dir_root = './sim_data/'
    diff_data_list = []
    for i in model_list:
        data_dir = data_dir_root + i
        data_list = os.listdir(data_dir)
        for j in data_list:
            if j == "diff.npy":
                diff_data_list.append(os.path.join(data_dir, j))
    for i in diff_data_list:
        data = np.load(i)
        for i in range(len(show_datas)):
            show_datas[i].append(data[:, i])
    
    # print_list = ['x', 'y', 'z', 'wx', 'wy', 'wz']
    print_list = ['r', 'theta']
    for i,j in enumerate(show_datas):
        for m,data in enumerate(j):
            b.add_data(data, model_list[m]+'_'+print_list[i])
    b.show()    

    # datalist = os.listdir(data_dir)
    # rm_list = []
    # for i in datalist:
    #     if os.path.splitext(i)[1] != '.npy':
    #         rm_list.append(i)
    # for i in rm_list:
    #     datalist.remove(i)
    # sorted(datalist)
    # datalist.sort()
    # print(datalist)


    # for i in datalist:
    #     b.add_data(np.load(os.path.join(data_dir, i))[:,data_type], i.replace('.npy', '')[4:])
    #     # b.add_data(np.load(os.path.join(data_dir, i))[:,data_type], i.replace('.npy', '')[4:])
    # # b.data = b.data[['VAE_0', 'VAE_10', 'VAE_1', 'PPA_0', 'PPA_10', 'PPA_1','ADP_0', 'ADP_10', 'ADP_1']]
    # b.show()

def eval_force(form="sim", model_list=['6dof', '2dof']):
    b = BoxPlot('Force', 'model', 'N/(N·m)')
    show_datas = [[],[],[]]
    for model in model_list:
        g = os.walk(f'./{form}_data/{model}')
        data_list = []
        for p_dir, c_dir, files in g:
            for file in files:
                if (form == "real" and os.path.splitext(file)[1] == '.npy') or \
                   (form == "sim" and file == "force.npy"):
                        data_list.append(os.path.join(p_dir, file))

        force_datas = np.empty((0,3))
        torque_datas = np.empty((0,3))
        for i in data_list:
            data = np.load(i)

            force_datas = np.concatenate((force_datas, data[:, :3]), axis=0)
            torque_datas = np.concatenate((torque_datas, data[:, 3:]), axis=0)

        sum_datas = np.concatenate((force_datas, torque_datas), axis=1)
        # ic(force_datas, torque_datas, sum_datas)
        force_datas = np.abs(np.sum(force_datas, axis=1))
        torque_datas = np.abs(np.sum(torque_datas, axis=1))
        sum_datas = np.abs(np.sum(sum_datas, axis=1))
        show_datas[0].append(force_datas)
        show_datas[1].append(torque_datas)
        show_datas[2].append(sum_datas)
        # ic(force_datas, torque_datas, sum_datas)
    print_list = ['f', 't', 's'] # force, torque, sum
    for i,j in enumerate(show_datas):
        for m,data in enumerate(j):
            b.add_data(data, model_list[m]+'_'+print_list[i])
    b.show()

if __name__ == '__main__':
    eval_force('sim',['ppo','adp','ppa'])
    # eval_sim(['ppo', 'ppa', 'adp'])

    # show_train_curve
    # c = CurveVis(
    #     curve_file=['/home/luckky/train_curve_data/6dof','/home/luckky/train_curve_data/2dof'],
    #     data_form='tb',
    #     y_label='reward',
    #     labels=['ppo_6dof','ppo_2dof'],
    #     smooth_k=7)
    # c.show()
    
    # eval_sim('./sim_data', 0)
    # eval_sim('./sim_data', 1)