import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/screens/plaid.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

Future main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  await dotenv.load(fileName: ".env");
  runApp(const SmartFin());
}

class SmartFin extends StatelessWidget {
  const SmartFin({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SmartFin',
      theme: ThemeData(
        colorScheme: const ColorScheme.dark(),
        useMaterial3: true,
      ),
      home: const Plaid(),
    );
  }
}
