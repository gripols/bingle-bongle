import PencilKit
import UIKit

class PencilKitHelper {
    
    static func createCanvas() -> PKCanvasView {
        let canvasView = PKCanvasView()
        canvasView.backgroundColor = .white
        canvasView.isOpaque = false
        return canvasView
    }
    
    static func saveDrawing(canvasView: PKCanvasView) -> Data? {
        do {
            let data = try canvasView.drawing.dataRepresentation()
            return data
        } catch {
            print("Error saving drawing: \(error)")
            return nil
        }
    }
    
    static func loadDrawing(from data: Data, canvasView: PKCanvasView) {
        do {
            let drawing = try PKDrawing(data: data)
            canvasView.drawing = drawing
        } catch {
            print("Error loading drawing: \(error)")
        }
    }
    
    static func clearCanvas(canvasView: PKCanvasView) {
        canvasView.drawing = PKDrawing()
    }
}