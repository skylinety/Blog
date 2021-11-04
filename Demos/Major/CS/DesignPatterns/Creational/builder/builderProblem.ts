class House {
  public windows: string[] = [];
  public doors: string[] = [];
  public rooms: string[] = [];
  public area: number = 0;
  public parts: string[] = [];
  constructor() {
    this.setWindows("window");
    this.setDoors("door");
    this.setBedRooms("room");
  }
  public listWindows(): House {
    console.log(`House windows: ${this.windows.join(", ")}\n`);
    return this;
  }
  public listDoors(): House {
    console.log(`House doors: ${this.doors.join(", ")}\n`);
    return this;
  }
  public listRooms(): House {
    console.log(`House rooms: ${this.rooms.join(", ")}\n`);
    return this;
  }

  public setWindows(w: string): House {
    this.windows.push(w);
    return this;
  }
  public setDoors(d: string): House {
    this.doors.push(d);
    return this;
  }
  public setBedRooms(r: string): House {
    this.rooms.push(r);
    this.area += 30;
    return this;
  }
  public setKitchens(r: string): House {
    this.rooms.push(r);
    this.area += 20;
    return this;
  }
  public capacity(): number {
    return this.area / 15;
  }
}
class HouseWithGarage extends House {
  constructor() {
    super();
    this.setGarges("garage");
  }
  public listGarges(): House {
    console.log(`House parts: ${this.parts.join(", ")}\n`);
    return this;
  }
  public setGarges(g: string): House {
    this.parts.push(g);
    return this;
  }
}

const hg = new HouseWithGarage();
console.log("builderProblem.ts第63行:::hg", hg);
// {
//   "windows": [
//     "window"
//   ],
//   "doors": [
//     "door"
//   ],
//   "rooms": [
//     "room"
//   ],
//   "area": 30,
//   "parts": [
//     "garage"
//   ]
// }
