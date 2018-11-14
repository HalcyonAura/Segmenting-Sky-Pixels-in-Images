%%% This script binarizes results from the cityscapes model

clear all;close all;

prediction_dir = 'Path/to/predicted/results';
ground_truths_dir = 'Path/to/ground/truths';
out_dir = 'Path/to/output/dir';

folders = dir(prediction_dir);

k=1;

%remove '.' and '..' from directories
folders=folders(~ismember({folders.name},{'.','..'})); 
%split 1:22443

for j = 1:length(folders)
    disp(folders(j).name);
     prediction_dir2 = fullfile(prediction_dir,folders(j).name);
    pred_files = dir(prediction_dir2);
    %remove '.' and '..' from directories
    pred_files=pred_files(~ismember({pred_files.name},{'.','..'}));
   
    for i=1:length(pred_files)
        % for loop through images
        %disp(fullfile(prediction_dir,folders(j).name,pred_files(i).name()));
        gt_map = imread(fullfile(prediction_dir,folders(j).name,pred_files(i).name()));
        disp(gt_map)
        %read maps
        %if(~exist(fullfile(out_dir,folders(j).name),'dir'))
        %    mkdir(fullfile(out_dir,folders(j).name))
        %end
        %imwrite(gt_map, fullfile(out_dir,folders(j).name,pred_files(i).name));
    end
end