def compute_a121_fixed_step(start_m, end_m, step_length):
    """
    Computes A121 radar parameters for fixed step_length = 2.5mm

    Args:
        start_m (float): Start range in meters
        end_m (float): End range in meters

    Returns:
        dict: {
            'start_point': int,
            'num_points': int,
            'step_length': float (always 0.0025),
            'end_m_adjusted': float
        }
    """
    STEP_LENGTH = 0.0025 * step_length  # fixed 2.5mm
    
    # Calculate start_point
    start_point = int(round((start_m) / STEP_LENGTH))
    end_point = int(round((end_m) / STEP_LENGTH))

    num_points = end_point - start_point + 1

    if num_points <= 0:
        raise ValueError("end_m must be greater than start_m with fixed 2.5mm step.")

    # 실제 적용되는 end_m 계산
    end_m_adjusted = STEP_LENGTH * (start_point + num_points - 1)

    return {
        'start_point': start_point,
        'num_points': num_points,
        'step_length': STEP_LENGTH,
        'end_m_adjusted': end_m_adjusted
    }

print("give a start meter : ")
start_m = float(input())
print("input a end meter : ")
end_m = float(input())
print("input a step length : ")
step_length = int(input())

result = compute_a121_fixed_step(start_m, end_m, step_length)
print(result)