//
//  bingle_bongleApp.swift
//  bingle-bongle
//
//  Created by Oleg Polstvin on 2025-10-04.
//

import SwiftUI
import CoreData

@main
struct bingle_bongleApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
