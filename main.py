# import standard libraries
from geometry.cylinder import volume_cylinder
from geometry.box import volume_box
from geometry.cone import volume_cone
from geometry.sphere import volume_sphere

def menu():
    print("\n=== 3D Geometry Volume Calculator ===")
    print("1. Volume of a Cylinder")
    print("2. Volume of a Box")
    print("3. Volume of a Cone")
    print("4. Volume of a Sphere")
    print("5. Quit")

def run():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            r = float(input("Enter radius (m): "))
            h = float(input("Enter height (m): "))
            v = volume_cylinder(r, h)
            print(f"Volume of cylinder: {v:.3f} m³")

        elif choice == "2":
            w = float(input("Enter width (m): "))
            h = float(input("Enter height (m): "))
            d = float(input("Enter depth (m): "))
            v = volume_box(w, h, d)
            print(f"Volume of box: {v:.3f} m³")

        elif choice == "3":
            r = float(input("Enter radius (m): "))
            h = float(input("Enter height (m): "))
            v = volume_cone(r, h)
            print(f"Volume of cone: {v:.3f} m³")

        elif choice == "4":
            r = float(input("Enter radius (m): "))
            v = volume_sphere(r)
            print(f"Volume of sphere: {v:.3f} m³")

        elif choice == "5":
            print("Catch you later, mate!\n\n")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run()
