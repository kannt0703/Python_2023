
import json

class Dataset:
    def __init__(self):
        print("Dataset Class Initialized")
        self.feature_names = []# Để so sánh và trực quan hóa tính năng
        """
            Lưu trữ dữ liệu lịch sử thô của một loại tiền cụ thể ở định dạng JSON 
        """
    def storeRawCoinHistoricData(self, name, coin_name, data):
        print("Storing Raw Historic Data for ", coin_name)
        with open("Raw historic data/ " + name + " " + coin_name + ".json", "w") as outfile:
            json.dump(data, outfile)
        """
            Tải dữ liệu lịch sử thô của một loại tiền cụ thể và chuyển đổi sang định dạng JSON
        """
    def loadRawCoinHistoricDatat(self, coin_name):
        print("Loading Raw Historic Data for ", coin_name)
        data = None
        with open("Rraw historic data/ " + coin_name + ".json", ) as json_file:
            data = json.load(json_file)
        return data
    """
        Tải tất cả dữ liệu xu, trong các tháng đã chọn, vào một mảng được sắp xếp.
        Mỗi hàng đại diện cho trạng thái của đồng xu mỗi phút.
    """        
    def loadCoinData(self):
        pass
    def createTrainTestSets(self):
        pass
