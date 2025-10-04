import SwiftUI

struct MainView: View {
    @State private var notes: [Note] = []
    @State private var showHandwritingView = false

    var body: some View {
        NavigationView {
            VStack {
                List(notes) { note in
                    NavigationLink(destination: HandwritingView(note: note)) {
                        Text(note.title)
                    }
                }
                .navigationTitle("Bingle Bongle Notes")
                
                Button(action: {
                    showHandwritingView.toggle()
                }) {
                    Text("Create New Note")
                        .font(.headline)
                        .padding()
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
                .sheet(isPresented: $showHandwritingView) {
                    HandwritingView(note: Note(title: "New Note", content: ""))
                }
            }
        }
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        MainView()
    }
}