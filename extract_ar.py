keys = "VStr vNum EegMeg nChan_extra trigPoint dType num_elec data_pts".split()
ERP_dict = dict(zip(keys,struct.unpack_from(">7sh6f",open(r.AR_file,"rb").read())))

avgmat_length_str ='>7sh6f' + str(int(ERP_dict["num_elec"]*ERP_dict["data_pts"])) + 'f'

fid = open(r.AR_file,"rb").read()
all_dat = struct.unpack_from(avgmat_length_str, fid)
avg_mat = all_dat[8:]
