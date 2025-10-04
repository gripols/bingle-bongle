import SwiftUI
import PencilKit

struct HandwritingView: View {
    @State private var canvasView = PKCanvasView()
    @State private var drawing = PKDrawing()
    
    var body: some View {
        VStack {
            CanvasView(canvasView: $canvasView, drawing: $drawing)
                .background(Color.white)
                .border(Color.gray, width: 1)
                .padding()
            
            Button(action: saveDrawing) {
                Text("Save Drawing")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }
        }
        .navigationTitle("Handwriting Input")
        .onAppear {
            setupCanvas()
        }
    }
    
    private func setupCanvas() {
        canvasView.delegate = context.coordinator
        canvasView.drawing = drawing
        canvasView.isUserInteractionEnabled = true
    }
    
    private func saveDrawing() {
        // Implement save functionality here
    }
    
    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    class Coordinator: NSObject, PKCanvasViewDelegate {
        var parent: HandwritingView
        
        init(_ parent: HandwritingView) {
            self.parent = parent
        }
        
        func canvasViewDrawingDidChange(_ canvasView: PKCanvasView) {
            parent.drawing = canvasView.drawing
        }
    }
}

struct CanvasView: UIViewRepresentable {
    @Binding var canvasView: PKCanvasView
    @Binding var drawing: PKDrawing
    
    func makeUIView(context: Context) -> PKCanvasView {
        return canvasView
    }
    
    func updateUIView(_ uiView: PKCanvasView, context: Context) {
        uiView.drawing = drawing
    }
}