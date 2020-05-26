class DataAnamorphosis:
    def __init__(self):
        self.objects = []
        self.selectedId = None
        self.selectedIdx = 0
        
        self.fig = None
        self.ani = None
        self.axis = "x-akse"
        
        # Synsvinkel.
        self.azim = -40
        self.elev = 10
        self.dist = 10
        self.axesLim = 10
        self.hud_visible = True

        # Antal rotationer til en hel omgang.
        self.rotation_step = 0.2

    def add_object(self, obj):
        self.objects.append(obj)

    def set_selected_id(self, selectedId):
        self.selectedId = selectedId
        self.selectedIdx = self.get_selected_idx()

    def get_selected_idx(self):
        for i in range(len(self.objects)):
            if str(self.objects[i].id) == str(self.selectedId):
                return i

    def get_objects(self):
        return self.objects

    def get_objs_of_type(self, objType: str):
        objects = []
        for obj in self.objects:
            if obj.objType == objType:
                objects.append(obj)
        return objects