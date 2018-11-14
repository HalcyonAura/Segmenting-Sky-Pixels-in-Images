
% Author: Guosheng Lin (guosheng.lin@gmail.com)

% perform segmentation prediction on user provided images.
% specify the location of your images, e.g., using the following 
% folder which contains serveral example images:
% ds_config.img_data_dir='../datasets/custom_data';


function demo_refinenet_test_example_SkyFinderLoop()
folders = {'861','8953','9708'};
%folders = {'858','1093','3837','3395','5020','4801','8438','8733','4679','9291','10917','17218','17244','75','204','861','3297','4232','6798','8953','9112','9708','11331','162','4795','5021','11160','19306'}
%folders ={'65','260','623','684','3396','3888','4181','4584','7211','7233','7371','8733','9291','9483','9730','10066','10870','17244','19106','19388'}
for i=1:length(folders)

rng('shuffle');

addpath('./my_utils');
dir_matConvNet='../libs/matconvnet/matlab';
run(fullfile(dir_matConvNet, 'vl_setupnn.m'));


run_config=[];
ds_config=[];

%run_config.use_gpu=true;
 run_config.use_gpu=false;
%run_config.gpu_idx=1;



% result dir:
%result_name=['result_' datestr(now, 'YYYYmmDDHHMMSS') '_evaonly_custom_data'];
result_name=char(folders(i));
result_dir=fullfile('../cache_data', result_name);


% the folder that contains testing images:
ds_config.img_data_dir=fullfile('../datasets/example_imgs_cityscapes',char(folders(i)));
% using a trained model which is trained on VOC 2012
run_config.trained_model_path='../model_trained/refinenet_res101_cityscapes.mat'; % resnet101 based refinenet
ds_config.class_info=gen_class_info_cityscapes();




% for voc trained model, control the size of input images
run_config.input_img_short_edge_min=227;
run_config.input_img_short_edge_max=227;

% set the input image scales, useful for multi-scale evaluation
% e.g. using multiple scale settings (1.0 0.8 0.6) and average the resulting score maps.
run_config.input_img_scale=0.8;


run_config.gen_net_opts_fn=@gen_net_opts_model_type1;


run_config.run_evaonly=true;
ds_config.use_custom_data=true;
ds_config.use_dummy_gt=true;
run_config.use_dummy_gt=ds_config.use_dummy_gt;


ds_config.ds_name='tmp_data';
run_config.root_cache_dir=result_dir;
mkdir_notexist(run_config.root_cache_dir);

run_config.model_name=result_name;

diary_dir=run_config.root_cache_dir;
mkdir_notexist(diary_dir);
diary(fullfile(diary_dir, 'output.txt'));
diary on


run_dir_name=fileparts(mfilename('fullpath'));
[~, run_dir_name]=fileparts(run_dir_name);
run_config.run_dir_name=run_dir_name;
run_config.run_file_name=mfilename();

ds_info=gen_dataset_info(ds_config);
my_diary_flush();

train_opts=run_config.gen_net_opts_fn(run_config, ds_info.class_info);


imdb=my_gen_imdb(train_opts, ds_info);

data_norm_info=[];
data_norm_info.image_mean=128;

imdb.ref.data_norm_info=data_norm_info;

if run_config.use_gpu
	gpu_num=gpuDeviceCount;
	if gpu_num>=1
		gpuDevice(run_config.gpu_idx);
    else
        error('no gpu found!');
	end
end

[net_config, net_exp_info]=prepare_running_model(train_opts);

my_net_tool(train_opts, imdb, net_config, net_exp_info);


fprintf('\n\n--------------------------------------------------\n\n');
disp('results are saved in:');
disp(run_config.root_cache_dir);


my_diary_flush();
diary off


end

end

