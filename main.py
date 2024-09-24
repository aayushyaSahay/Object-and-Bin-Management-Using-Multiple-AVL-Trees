from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException
if __name__=="__main__":

    gcms = GCMS()
    
    gcms.add_bin(1234, 10)
    gcms.add_bin(4321, 20)
    gcms.add_bin(1111, 15)

    print(gcms.bins_by_id.in_order_traversal())
    print(gcms.bins_by_capacity.in_order_traversal())
    
    try:
        gcms.add_object(8989, 6, Color.BLUE)
    except: 
        print("Object 1 was not able to be added")
    
    print("Status of bins")
    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
    print(gcms.objects_by_id.in_order_traversal())
    print("")
    

    try:
        gcms.add_object(2892, 8, Color.BLUE )
    except: 
        print("Object 2 was not able to be added")
    
    print("Status of bins")
    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
    print(gcms.objects_by_id.in_order_traversal())
    print("")

    try:
        gcms.add_object(4839, 9, Color.BLUE )
    except: 
        print("Object 3 was not able to be added")

    print("Status of bins")
    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
    print(gcms.objects_by_id.in_order_traversal())
    print("")

    try:
        gcms.add_object(3283, 2, Color.BLUE )
    except: 
        print("Object 4 was not able to be added")

    print("Status of bins")
    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
    print(gcms.objects_by_id.in_order_traversal())
    print("")

    
    try:
        gcms.add_object(8983, 8, Color.BLUE )
    except: 
        print("Object 5 was not able to be added")

    
    print("Status of bins")
    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
    print(gcms.objects_by_id.in_order_traversal())
    print("")

    print(gcms.object_info(3283))
    print(gcms.object_info(2892))
    print(gcms.object_info(4839))
    print(gcms.object_info(8983))
    print(gcms.object_info(8989))

    try:
        gcms.delete_object(3283)
    except:
        print("couldn't delete")

    try:
        gcms.delete_object(2892)
    except:
        print("couldn't delete")

    try:
        gcms.delete_object(4839)
    except:
        print("couldn't delete")

    try:
        gcms.delete_object(8983)
    except:
        print("couldn't delete")
    try:
        gcms.delete_object(8989)
    except:
        print("couldn't delete")