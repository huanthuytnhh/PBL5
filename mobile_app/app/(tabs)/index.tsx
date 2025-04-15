import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Image } from 'react-native';
import { ChevronRight, Sun, Moon, Wind, Thermometer } from 'lucide-react-native';

export default function HomeScreen() {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.greeting}>Welcome Home</Text>
        <Text style={styles.subGreeting}>Good morning, User</Text>
      </View>

      <View style={styles.quickStats}>
        <View style={styles.statCard}>
          <Thermometer size={24} color="#007AFF" />
          <Text style={styles.statValue}>23°C</Text>
          <Text style={styles.statLabel}>Temperature</Text>
        </View>
        <View style={styles.statCard}>
          <Wind size={24} color="#32ADE6" />
          <Text style={styles.statValue}>65%</Text>
          <Text style={styles.statLabel}>Humidity</Text>
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Quick Actions</Text>
        <View style={styles.quickActions}>
          <TouchableOpacity style={styles.actionButton}>
            <Sun size={24} color="#FFB800" />
            <Text style={styles.actionText}>Day Mode</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.actionButton}>
            <Moon size={24} color="#5856D6" />
            <Text style={styles.actionText}>Night Mode</Text>
          </TouchableOpacity>
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Rooms</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.roomsScroll}>
          {['Living Room', 'Kitchen', 'Bedroom', 'Bathroom'].map((room, index) => (
            <TouchableOpacity key={room} style={styles.roomCard}>
              <Image
                source={{ uri: `https://source.unsplash.com/300x200/?${room.toLowerCase().replace(' ', '-')}` }}
                style={styles.roomImage}
              />
              <Text style={styles.roomName}>{room}</Text>
              <ChevronRight size={16} color="#8E8E93" style={styles.chevron} />
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F2F2F7',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#ffffff',
  },
  greeting: {
    fontSize: 28,
    fontWeight: '700',
    color: '#000000',
  },
  subGreeting: {
    fontSize: 16,
    color: '#8E8E93',
    marginTop: 4,
  },
  quickStats: {
    flexDirection: 'row',
    padding: 20,
    justifyContent: 'space-between',
  },
  statCard: {
    backgroundColor: '#ffffff',
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    width: '48%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  statValue: {
    fontSize: 24,
    fontWeight: '600',
    marginTop: 8,
    color: '#000000',
  },
  statLabel: {
    fontSize: 14,
    color: '#8E8E93',
    marginTop: 4,
  },
  section: {
    padding: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    marginBottom: 16,
    color: '#000000',
  },
  quickActions: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  actionButton: {
    backgroundColor: '#ffffff',
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    width: '48%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  actionText: {
    marginTop: 8,
    fontSize: 14,
    color: '#000000',
  },
  roomsScroll: {
    marginHorizontal: -20,
    paddingHorizontal: 20,
  },
  roomCard: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    marginRight: 16,
    width: 160,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  roomImage: {
    width: '100%',
    height: 100,
    borderTopLeftRadius: 12,
    borderTopRightRadius: 12,
  },
  roomName: {
    fontSize: 14,
    fontWeight: '500',
    padding: 12,
    color: '#000000',
  },
  chevron: {
    position: 'absolute',
    right: 12,
    bottom: 12,
  },
});