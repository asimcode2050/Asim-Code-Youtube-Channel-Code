# Python Script to Display Segment Addresses
import pefile


def display_section_addresses(exe_path):
    pe = pefile.PE(exe_path)
    print(f"PE File: {exe_path}")
    print(f"Number of Sections: {len(pe.sections)}")
    for section in pe.sections:
        print(f"Section: {section.Name.decode('utf-8').strip()}")
        print(f"  Virtual Address: 0x{section.VirtualAddress:08X}")
        print(f"  Virtual Size: 0x{section.Misc_VirtualSize:08X}")
        print(f"  Raw Data Size: 0x{section.SizeOfRawData:08X}")
        print(f"  Raw Data Pointer: 0x{section.PointerToRawData:08X}")
        print("-" * 40)


exe_path = r'C:\windows\system32\notepad.exe'
display_section_addresses(exe_path)
