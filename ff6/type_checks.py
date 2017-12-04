from ff6.data import check_data_value, check_data_member

def _get_range_checker(min_val, max_val):
    def range_checker(name, val):
        val = int(val)
        if val < min_val or val > max_val:
            msg = 'Value for %s out of range (%d, %d): %d'
            raise ValueError(msg  % (name, min_val, max_val, val))
    return range_checker

check_u3  = _get_range_checker(0, 7)
check_u4  = _get_range_checker(0, 15)
check_u5  = _get_range_checker(0, 31)
check_s4  = _get_range_checker(-8, 7)
check_u8  = _get_range_checker(0, 255)
check_s8  = _get_range_checker(-128, 127)
check_u16 = _get_range_checker(0, 65535)
check_s16 = _get_range_checker(-32768, 32767)
check_str = lambda name, val: str(val)
check_enum_value = lambda e: lambda name, val: check_data_value(name, val, e)
check_enum_member = lambda e: lambda name, val: check_data_member(name, val, e)

def check_bool(name, val):
    if not isinstance(val, bool):
        msg = 'Value for %s should be bool, got %s (%s)'
        raise ValueError(msg % (name, type(val), val))
