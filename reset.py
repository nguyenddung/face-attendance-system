import os
import shutil
import csv


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def reset_file(path, headers=None):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if headers:
            writer.writerow(headers)


def reset_system():
    print("🧹 BẮT ĐẦU RESET TOÀN BỘ HỆ THỐNG...\n")

    # 1. Xóa & tạo lại thư mục lưu ảnh khuôn mặt
    train_img_path = "TrainingImage"
    if os.path.exists(train_img_path):
        shutil.rmtree(train_img_path)
    ensure_dir(train_img_path)
    print("✅ Đã reset thư mục TrainingImage/")

    # 2. Xóa & tạo lại mô hình huấn luyện
    train_label_folder = "TrainingImageLabel"
    train_model_path = os.path.join(train_label_folder, "Trainner.yml")
    if os.path.exists(train_model_path):
        os.remove(train_model_path)
    ensure_dir(train_label_folder)
    print("✅ Đã reset TrainingImageLabel/ và xóa Trainner.yml")

    # 3. Xóa & tạo lại danh sách sinh viên CSV
    student_folder = "StudentDetails"
    student_csv = os.path.join(student_folder, "studentdetails.csv")
    if os.path.exists(student_csv):
        os.remove(student_csv)
    ensure_dir(student_folder)
    reset_file(student_csv, headers=["Enrollment", "Name"])
    print("✅ Đã reset StudentDetails/studentdetails.csv")

    # 4. Xóa & tạo lại thư mục điểm danh
    attendance_folder = "Attendance"
    if os.path.exists(attendance_folder):
        shutil.rmtree(attendance_folder)
    ensure_dir(attendance_folder)
    print("✅ Đã reset thư mục Attendance/")

    # 5. (Tuỳ chọn) Tạo thư mục điểm danh thủ công nếu có
    manual_attendance = "Attendance(Manually)"
    if os.path.exists(manual_attendance):
        shutil.rmtree(manual_attendance)
    ensure_dir(manual_attendance)
    print("✅ Đã reset thư mục Attendance(Manually)/")

    print("\n🎉 HỆ THỐNG ĐÃ ĐƯỢC RESET HOÀN TOÀN VỀ TRẠNG THÁI BAN ĐẦU.")


if __name__ == "__main__":
    reset_system()
