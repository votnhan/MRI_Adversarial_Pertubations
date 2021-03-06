import torch.nn.functional as F
import torch


def class_to_one_hot(target, num_classes=4):
    """
    :param target: shape: (N, W, H)
    :param num_classes: number of class
    :return: one_hot encoder of target
    """
    long_ts = target.type(torch.LongTensor).cuda()
    one_hot = F.one_hot(long_ts, num_classes)
    channels_first = torch.transpose(one_hot, 1, 3)
    reverse_spatial = torch.transpose(channels_first, 2, 3)
    return reverse_spatial


def check_nan_tensor(tensor):
    result = torch.isnan(tensor)
    isnan = torch.sum(result)
    if isnan.item() != 0:
        return True
    return False


def normalized_softmax(tensor, dim):
    max_val = torch.max(tensor)
    diff_max = tensor - max_val
    return F.softmax(diff_max, dim)