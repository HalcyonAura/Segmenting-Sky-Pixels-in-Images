% Given folders within a dataset and a list of segmentations per camera(ie SkyFinder)
% this code will create copies of segmentations to match the dataset
% in order for RefineNet to use the dataset

in_path = 'Path/to/dataset';
out_path = 'Path/to/segmentations/';

in_folders = dir(in_path);
out_folders = dir(out_path);

for i=3:length(in_folders)
    temp = in_folders(i).name;
    if(~contains(temp, '.txt'))
        cam_name = extractBetween(temp, 4, length(temp));
        folder_name = strcat(out_path, cam_name);
        mkdir folder_name
        
        disp(temp);
    end
end
print out