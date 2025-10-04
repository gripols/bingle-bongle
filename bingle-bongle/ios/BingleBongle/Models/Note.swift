import Foundation

struct Note: Codable {
    var title: String
    var content: String
    var timestamp: Date

    init(title: String, content: String, timestamp: Date = Date()) {
        self.title = title
        self.content = content
        self.timestamp = timestamp
    }
}