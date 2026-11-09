import multiprocessing
import time
import sys

def run_bot(bot_id):
    bot_name = f"KTech_Bot_{bot_id}"
    print(f"🤖 [{bot_name}] Đang khởi động và chuẩn bị kết nối...")
    
    # Giả lập thời gian kết nối vào phòng họp
    time.sleep(2)
    print(f"✅ [{bot_name}] Đã vào phòng thành công với tên '{bot_name}'!")
    
    # Giả lập bot duy trì trong phòng họp (ví dụ: hoạt động trong 10 giây rồi thoát)
    try:
        for i in range(5):
            print(f"🔄 [{bot_name}] Đang hoạt động... bước {i+1}/5")
            time.sleep(2)
    except KeyboardInterrupt:
        pass
        
    print(f"❌ [{bot_name}] Đã rời khỏi phòng họp.")

if __name__ == "__main__":
    # Số lượng bot bạn muốn chạy đồng thời (ở đây để 3 bot, bạn có thể đổi từ 1 đến 5)
    NUM_BOTS = 3
    
    print(f"🚀 Bắt đầu khởi chạy binh đoàn gồm {NUM_BOTS} bot...")
    processes = []

    # Tạo và chạy từng bot song song
    for i in range(1, NUM_BOTS + 1):
        p = multiprocessing.Process(target=run_bot, args=(i,))
        processes.append(p)
        p.start()

    # Chờ tất cả các bot chạy xong
    for p in processes:
        p.join()

    print("🏁 Tất cả các bot đã hoàn thành phiên làm việc!")
  
